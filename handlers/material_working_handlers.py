from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.inline.kb_generators import navigate_kb
from repository.material_repository import Materials
from repository.redis_pages_repository import PagesRepository
from repository.model_formatting_utils import get_material_from_message,get_tg_list_from_tuple
from fsm_states.action_state import FSMActionStates

from filters.text_theory_filter import ShowTextTheoryFilter

from utils.work_funcs import get_actual_type


router: Router = Router()
m_rep: Materials = Materials()
p_rep: PagesRepository = PagesRepository()

# todo ВЫНЕСТИ КОНСТАНТУ В ДРУГОЕ МЕСТО
RECORDS_COUNT = 10


@router.callback_query(ShowTextTheoryFilter(
    updates=["add_text", "add_theory"]))
async def add_text_chosen(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMActionStates.new_material)
    await state.update_data(type=get_actual_type(callback=callback))
    await callback.message.answer("Отправьте ваше сообщение, которое пойдет в народ")
    await callback.answer()


@router.callback_query(ShowTextTheoryFilter(
    updates=["delete_text", "delete_theory"]))
async def delete_material_chosen(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMActionStates.delete_material)
    await state.update_data(type=get_actual_type(callback=callback))
    await callback.message.answer("Отправьте номер заметки, которую вы бы хотели удалить")
    await callback.answer()


@router.callback_query(ShowTextTheoryFilter(
    updates=["show_own_text", "show_own_theory"]))
async def show_own_material(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMActionStates.show_own_material)
    print(callback.json())
    type = get_actual_type(callback=callback)
    result = m_rep.get_own_materials(r_count=RECORDS_COUNT,
                                     type=type,
                                     telegram_id=callback.from_user.id)
    answer = get_tg_list_from_tuple(materials=result,
                                    r_count=RECORDS_COUNT)
    if len(result) > 0:
        state = m_rep.count_user_material(type=type,
                                          telegram_id=callback.from_user.id) > 10
        if state:
            if p_rep.exists(key=callback.from_user.id,
                            type=type):
                page = int(p_rep.get(key=callback.from_user.id,
                                     type=type))
            else:
                p_rep.add(key=callback.from_user.id,
                          type=type,
                          value=1)
                page = 1
        else:
            page = None
        p_rep.add(key=callback.from_user.id,
                  type=type,
                  value=1)
        await callback.message.answer(text=f"{answer}",
                                      reply_markup=navigate_kb(state=state,
                                                               page=page,
                                                               type=type))
        await callback.answer()
    await callback.answer("Ничего еще не добавлено")


@router.message(FSMActionStates.new_material)
async def add_material(message: Message, state: FSMContext):
    type = await state.get_data()
    type = type["type"]
    m_rep.add_material(get_material_from_message(message, type=type))
    await message.answer("Успешно добавлено")
    await state.clear()


@router.message(FSMActionStates.delete_material)
async def delete_material(message: Message, state: FSMContext):
    type = await state.get_data()
    type = type["type"]
    if message.text.isdigit():
        if m_rep.count_user_material(type=type,
                                     telegram_id=message.from_user.id) >= int(message.text) > 0:
            m_rep.delete_material(material_id=m_rep.get_id_from_number(type=type,
                                                                       telegram_id=message.from_user.id,
                                                                       number=int(message.text)))
            await message.answer("Успешно удалено")
            await state.clear()
        else:
            await message.answer("Некорректный номер. Попробуй еще раз")
    else:
        await message.answer("Введите номер, которы желаете удалить")
