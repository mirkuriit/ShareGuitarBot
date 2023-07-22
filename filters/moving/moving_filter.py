from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class NoneMovingFilter(BaseFilter):
    def __init__(self, updates: list[str]):
        self.updates = updates

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data in self.updates


class MovingFilter(BaseFilter):
    def __init__(self, updates: list[str]):
        self.updates = updates

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data in self.updates


