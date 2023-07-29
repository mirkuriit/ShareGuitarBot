from aiogram.filters import Command, CommandStart, Text
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from lexicon.lexicon import COMMANDS_RU
from keyboards.inline.kb_generators import csd_kb, secret_kb
from repository.user_repository import Users
from repository.material_repository import Materials
from repository.model_formatting_utils import get_user_from_message, get_material_from_message
from fsm_states.action_state import FSMActionStates


router: Router = Router()
u_rep: Users = Users()


@router.message(CommandStart())
async def send_welcome(message: Message):
    user = get_user_from_message(message)
    if not u_rep.is_user_exists(message.from_user.id):
        u_rep.add_new_user(user)
    await message.reply(
        text=COMMANDS_RU[message.text]
    )


@router.message(Command(commands=["help"]))
async def send_commands_info(message: Message):
    await message.reply(
        text=COMMANDS_RU[message.text]
    )


@router.message(Command("text"))
async def send_text_info(message: Message):
    await message.reply(
        text=COMMANDS_RU[message.text],
        reply_markup=csd_kb(type="text")
    )


@router.message(Command("tabs"))
async def send_tabs_info(message: Message):
    await message.reply(
        text=COMMANDS_RU[message.text],
        reply_markup=csd_kb(type="tabs")
    )


@router.message(Command("links"))
async def send_theory_info(message: Message):
    await message.reply(
        text=COMMANDS_RU[message.text],
        reply_markup=csd_kb(type="theory")
    )

