from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardButton

from lexicon.lexicon import WELCOME_TTT


def csd_tabs_kb() -> InlineKeyboardMarkup:
    """csd - create/show/delete"""
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=WELCOME_TTT["show_own"], callback_data="show_own_tabs"),
        InlineKeyboardButton(text=WELCOME_TTT["show_public"], callback_data="show_public_tabs"),
        InlineKeyboardButton(text=WELCOME_TTT["add"], callback_data="add_tabs"),
        InlineKeyboardButton(text=WELCOME_TTT["delete"], callback_data="delete_tabs")
    ]

    return kb_builder.row(*buttons, width=1).as_markup()


def csd_theory_kb() -> InlineKeyboardMarkup:
    """csd - create/show/delete"""
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=WELCOME_TTT["show_own"], callback_data="show_own_theory"),
        InlineKeyboardButton(text=WELCOME_TTT["show_public"], callback_data="show_public_theory"),
        InlineKeyboardButton(text=WELCOME_TTT["add"], callback_data="add_theory"),
        InlineKeyboardButton(text=WELCOME_TTT["delete"], callback_data="delete_theory")
    ]

    return kb_builder.row(*buttons, width=1).as_markup()


def csd_text_kb() -> InlineKeyboardMarkup:
    """csd - create/show/delete"""
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=WELCOME_TTT["show_own"], callback_data="show_own_text"),
        InlineKeyboardButton(text=WELCOME_TTT["show_public"], callback_data="show_public_text"),
        InlineKeyboardButton(text=WELCOME_TTT["add"], callback_data="add_text"),
        InlineKeyboardButton(text=WELCOME_TTT["delete"], callback_data="delete_text")
    ]

    return kb_builder.row(*buttons, width=1).as_markup()


def navigate_text_kb(state: bool, page: str | int = "(-)") -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text="<-", callback_data="move_left_text"),
        InlineKeyboardButton(text=f"({page})", callback_data="move_none_text"),
        InlineKeyboardButton(text="->", callback_data="move_right_text"),
    ]
    markups = [None, kb_builder.row(*buttons, width=3).as_markup()]
    return markups[int(state)]


def navigate_theory_kb(state: bool, page: str | int = "(-)") -> InlineKeyboardMarkup | None:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text="<-", callback_data="move_left_theory"),
        InlineKeyboardButton(text=f"({page})", callback_data="move_none_theory"),
        InlineKeyboardButton(text="->", callback_data="move_right_theory"),
    ]
    markups = [None, kb_builder.row(*buttons, width=3).as_markup()]
    return markups[int(state)]


