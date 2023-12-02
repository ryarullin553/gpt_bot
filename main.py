import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import handlers
from config import BOT_TOKEN, DEBUG


async def main() -> None:
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode=ParseMode.MARKDOWN
    )
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)

    if DEBUG:
        logging.basicConfig(level=logging.INFO)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
