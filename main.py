import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import handlers
from config import BOT_TOKEN
from database import Database


async def main() -> None:
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode=ParseMode.MARKDOWN
    )
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)

    PLAYERS = []

    db = Database()
    await db.connect()
    try:
        await dp.start_polling(bot, db=db, players=PLAYERS)
    finally:
        await bot.session.close()
        await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
