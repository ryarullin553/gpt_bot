from aiogram import Router, F, types
from aiogram.enums import ChatAction
from aiogram.filters import Command
import traceback

from config import MY_ID
from constants import BotMessage
from gpt import get_answer

router = Router()


@router.message(Command('start'))
async def start(message: types.Message) -> None:
    """Приветственное сообщение с инструкцией по работе с ботом"""
    user_name: str = message.from_user.full_name
    await message.answer(text=BotMessage.START.format(user_name))


@router.message(F.text)
async def send_promt(message: types.Message) -> None:
    """Отправка промта с последующим получением ответа от GPT"""
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    tg_id: int = message.from_user.id
    if tg_id == int(MY_ID):
        response: str = await get_answer(message.text)
        try:
            await message.answer(text=response)
        except Exception:
            await message.answer(text=traceback.format_exc())
    else:
        await message.answer(text=BotMessage.NO_PERMISSION_ERROR)
