from aiogram import Router, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command

from constants import BotMessage
from gpt import get_answer

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    """Приветственное сообщение с инструкцией по работе с ботом"""
    user_name: str = message.from_user.full_name
    await message.answer(
        text=BotMessage.START.format(user_name),
        parse_mode=ParseMode.MARKDOWN
    )


@router.message(F.text)
async def send_promt(message: types.Message) -> None:
    """Отправка промта с последующим получением ответа от GPT"""
    response: str = await get_answer(message.text)
    await message.answer(
        text=response,
        parse_mode=ParseMode.MARKDOWN
    )