import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

import handlers
from config import BOT_TOKEN


async def main() -> None:
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode=ParseMode.MARKDOWN
    )
    dp = Dispatcher()
    dp.include_routers(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
