from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardButton

from lexicon.lexicon import WELCOME_TTT

from deprecated import deprecated


def _is_correct_type(type: str) -> bool:
    return type == "text" or type == "theory" or type == "tabs" or type == "files"


def csd_kb(type: str) -> InlineKeyboardMarkup | None:
    if _is_correct_type(type):
        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(text=WELCOME_TTT["show_own"], callback_data=f"show_own_{type}"),
            InlineKeyboardButton(text=WELCOME_TTT["show_public"], callback_data=f"show_public_{type}"),
            InlineKeyboardButton(text=WELCOME_TTT["add"], callback_data=f"add_{type}"),
            InlineKeyboardButton(text=WELCOME_TTT["delete"], callback_data=f"delete_{type}")
        ]
        return kb_builder.row(*buttons, width=1).as_markup()
    # todo добвить собственные ошибки в случае, если тип некорректный
    return None


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





