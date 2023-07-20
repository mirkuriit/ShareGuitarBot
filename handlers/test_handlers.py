from aiogram.filters import Command, CommandStart
from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import COMMANDS_RU
from repository.user_repository import Users
from repository.model_formatting_utils import get_user_from_message, get_material_from_message
from filters.admin_filter import IsAdmin

router: Router = Router()
u_rep: Users = Users()

@router.message(Command("delete"), IsAdmin())
async def delete_user(message: Message):
    u_rep.delete_user(int(message.from_user.id))


@router.message(Command("update"), IsAdmin())
async def update_count(message: Message):
    u_rep.update_useful_count(message.from_user.id)




