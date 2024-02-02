import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import CommandStart, Command
from config import TOKEN
from messages import MSG_ASSISTANT, CMD_CHAT
from handlers import cmd_start, chat


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(cmd_start.router, chat.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
