from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from repository.redis_pages_repository import PagesRepository
from repository.material_repository import Materials

from repository.model_formatting_utils import get_tg_list_from_tuple
from keyboards.inline.kb_generators import navigate_text_kb, navigate_theory_kb

from filters.no_moving_filter import NoneMovingFilter

router: Router = Router()
p_rep: PagesRepository() = PagesRepository()
m_rep: Materials() = Materials()

#todo переместить константу
RECORDS_COUNT = 10


def get_actual_page(telegram_id: int, type:str) -> int:
    return int(p_rep.get(key=telegram_id,
                         type=type))


@router.callback_query(Text("move_right_theory"))
async def move_text_right_chosen(callback: CallbackQuery, state:FSMContext):
    type = callback.data.split("_")[-1]
    max_page = m_rep.count_user_materials_pages(telegram_id=callback.from_user.id,
                                                type=type)
    page = get_actual_page(callback.from_user.id, type=type)
    print(type)
    if max_page > page:
        p_rep.increment(key=callback.from_user.id,
                        type=type)
        page = get_actual_page(callback.from_user.id, type=type)
        result = m_rep.get_own_materials(r_count=RECORDS_COUNT,
                                         type=type,
                                         telegram_id=callback.from_user.id,
                                         page=page)
        #print(page)
        #print(result)
        answer = get_tg_list_from_tuple(materials=result,
                                        r_count=RECORDS_COUNT,
                                        page=page)

        await callback.message.edit_text(text=f"{answer}",
                                         reply_markup=navigate_theory_kb(
                                         state=True,
                                         page=page
                                         ))
        await callback.answer()
    elif max_page == page:
        await callback.answer("Дальше некуда")


@router.callback_query(Text("move_left_theory"))
async def move_text_left_chosen(callback: CallbackQuery, state:FSMContext):
    # todo Вынести получение типа в отдельню функцию
    type = callback.data.split("_")[-1]
    page = get_actual_page(callback.from_user.id, type=type)
    if page == 1:
        await callback.answer("Дальше некуда")
    elif page > 1:
        p_rep.decr(key=callback.from_user.id,
                   type=type)
        page = get_actual_page(callback.from_user.id, type=type)
        result = m_rep.get_own_materials(r_count=RECORDS_COUNT,
                                         type=type,
                                         telegram_id=callback.from_user.id,
                                         page=page)
        #print(page)
        #print(result)
        answer = get_tg_list_from_tuple(materials=result,
                                        r_count=RECORDS_COUNT,
                                        page=page)
        await callback.message.edit_text(text=f"{answer}",
                                         reply_markup=navigate_theory_kb(
                                             state=True,
                                             page=page
                                        ))
        await callback.answer()


@router.callback_query(Text("move_right_theory"))
async def move_theory_right_chosen(callback: CallbackQuery, state:FSMContext):
    pass


@router.callback_query(Text("move_left_theory"))
async def move_theory_left_chosen(callback: CallbackQuery, state:FSMContext):
    pass


@router.callback_query(NoneMovingFilter(updates=["move_none_theory", "move_none_text"]))
async def move_none_chosen(callback: CallbackQuery, state:FSMContext):
    await callback.answer(":)")
