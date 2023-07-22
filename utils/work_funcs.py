from aiogram.types import CallbackQuery
from repository.redis_pages_repository import PagesRepository


def get_actual_page(telegram_id: int, type:str, p_rep: PagesRepository) -> int:
    return int(p_rep.get(key=telegram_id,
                         type=type))


def get_actual_type(callback: CallbackQuery) -> str:
    print(callback.data)
    return callback.data.split("_")[-1]