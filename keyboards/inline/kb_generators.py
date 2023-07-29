from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon import WELCOME_TTT

from deprecated import deprecated


def _is_correct_type(type: str) -> bool:
    return type == "text" or type == "theory" or type == "tabs" or type == "files"


def csd_kb(type: str) -> InlineKeyboardMarkup | None:
    if _is_correct_type(type):
        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(text=WELCOME_TTT["show_own"], callback_data=f"show_own_{type}",),
            InlineKeyboardButton(text=WELCOME_TTT["show_public"], callback_data=f"show_public_{type}"),
            InlineKeyboardButton(text=WELCOME_TTT["add"], callback_data=f"add_{type}"),
            InlineKeyboardButton(text=WELCOME_TTT["delete"], callback_data=f"delete_{type}")
        ]
        return kb_builder.row(*buttons, width=1).as_markup()
    # todo добвить собственные ошибки в случае, если тип некорректный
    return None

"""
def secret_kb() -> ReplyKeyboardMarkup:
    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb_builder.row(
        KeyboardButton(text="Пасхалка", request_location=True),
        KeyboardButton(text="Pashalka", request_contact=True)
    )
    return kb_builder.as_markup()
"""

def navigate_kb(state: bool, type: str, page: str | int = "(-)") -> InlineKeyboardMarkup | None:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    if _is_correct_type(type):
        buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(text="<-", callback_data=f"move_left_{type}"),
            InlineKeyboardButton(text=f"({page})", callback_data=f"move_none_{type}"),
            InlineKeyboardButton(text="->", callback_data=f"move_right_{type}"),
        ]
        markups = [None, kb_builder.row(*buttons, width=3).as_markup()]
        return markups[int(state)]
    # todo добвить собственные ошибки в случае, если тип некорректный
    return None





