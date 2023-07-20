from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class NoneMovingFilter(BaseFilter):
    def __init__(self, updates: list[str]):
        self.updates = updates

    async def __call__(self, callback: CallbackQuery)-> bool:
        # todo вынести захардкоденные строки куда-нибудь
        return callback.data in ["move_none_theory", "move_none_text"]
