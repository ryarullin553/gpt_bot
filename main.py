import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import handlers

load_dotenv()


async def main() -> None:
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
