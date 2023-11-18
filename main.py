import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram import F
from dotenv import load_dotenv

from constants import BotMessage
from gpt import get_answer


load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    """Приветственное сообщение с инструкцией по работе с ботом"""
    user_name: str = message.from_user.full_name
    await message.answer(
        text=BotMessage.START.format(user_name),
        parse_mode=ParseMode.MARKDOWN
    )


@dp.message(F.text)
async def send_promt(message: types.Message) -> None:
    """Отправка промта с последующим получением ответа от GPT"""
    response: str = await get_answer(message.text)
    await message.answer(
        text=response,
        parse_mode=ParseMode.MARKDOWN
    )


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
