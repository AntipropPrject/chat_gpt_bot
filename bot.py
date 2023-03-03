import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage

from handlers import main_handler

TOKEN = "6088452035:AAGiIUXnAQQcLMjIJxCrVr2-ZHeqFC_gmW8"
storage = RedisStorage.from_url("redis://redis")


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(main_handler.router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
