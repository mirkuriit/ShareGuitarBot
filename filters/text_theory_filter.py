from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class ShowTextTheoryFilter(BaseFilter):
    def __init__(self, updates: list[str]):
        self.updates = updates

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data in self.updates
