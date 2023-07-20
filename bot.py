import asyncio

from handlers import welcome_handlers, material_working_handlers, navigation_handlers
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config


async def main() -> None:
    config: Config = load_config(path="../.env")

    bot: Bot = Bot(token=config.bot.token)
    dp: Dispatcher = Dispatcher()
    dp.include_router(navigation_handlers.router)
    dp.include_router(welcome_handlers.router)
    #dp.include_router(test_handlers.router)
    dp.include_router(material_working_handlers.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


