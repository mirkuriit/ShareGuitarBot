from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from repository.redis_pages_repository import PagesRepository
from repository.material_repository import Materials

from repository.model_formatting_utils import get_tg_list_from_tuple
from keyboards.inline.kb_generators import navigate_kb

from filters.moving.moving_filter import NoneMovingFilter, MovingFilter

from utils.work_funcs import get_actual_page, get_actual_type

router: Router = Router()
p_rep: PagesRepository() = PagesRepository()
m_rep: Materials() = Materials()

#todo переместить константу
RECORDS_COUNT = 10


@router.callback_query(MovingFilter(
    updates=["move_right_text", "move_right_theory", "move_right_tabs", "move_right_file"]))
async def move_right_chosen(callback: CallbackQuery, state:FSMContext):
    type = get_actual_type(callback=callback)
    max_page = m_rep.count_user_materials_pages(telegram_id=callback.from_user.id,
                                                type=type)
    page = get_actual_page(telegram_id=callback.from_user.id,
                           type=type,
                           p_rep=p_rep)
    print(type)
    if max_page > page:
        p_rep.increment(key=callback.from_user.id,
                        type=type)
        page = get_actual_page(telegram_id=callback.from_user.id,
                               type=type,
                               p_rep=p_rep)
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
                                         reply_markup=navigate_kb(
                                            state=True,
                                            page=page,
                                            type=type
                                         ))
        await callback.answer()
    elif max_page == page:
        await callback.answer("Дальше некуда")


@router.callback_query(MovingFilter(
    updates=["move_left_text", "move_left_theory", "move_left_tabs", "move_left_file"]))
async def move_left_chosen(callback: CallbackQuery, state:FSMContext):
    type = get_actual_type(callback=callback)
    page = get_actual_page(telegram_id=callback.from_user.id,
                           type=type,
                           p_rep=p_rep)
    if page == 1:
        await callback.answer("Дальше некуда")
    elif page > 1:
        p_rep.decr(key=callback.from_user.id,
                   type=type)
        page = get_actual_page(telegram_id=callback.from_user.id,
                               type=type,
                               p_rep=p_rep)
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
                                         reply_markup=navigate_kb(
                                             state=True,
                                             page=page,
                                             type=type
                                        ))
        await callback.answer()


@router.callback_query(NoneMovingFilter(updates=["move_none_theory", "move_none_text"]))
async def move_none_chosen(callback: CallbackQuery, state:FSMContext):
    await callback.answer(":)")
