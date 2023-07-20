from aiogram.types import Message

from models.models import User, Material


def get_user_from_message(message: Message) -> User:
    return User(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username
    )


def get_material_from_message(message: Message, type: str) -> Material:
    if type == "text" or type == "theory":
        return Material(
            who_added=message.from_user.id,
            content=message.text,
            type=type
        )
    elif type == "tabs":
        # todo добавление табов
        pass


def get_tg_list_from_tuple(materials: list[tuple[str, str]], r_count: int, page: int=1) -> str:
    s = ""
    i=1
    print(page, "page")
    for content, date in materials:
        s += f"{r_count*(page-1)+i}){content}   {date.split(' ')[0]}\n\n"
        i += 1
    return s
