from aiogram import Router, F, types
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import Command

from constants import BotMessage, Query
from database import Database
from gpt import get_answer

router = Router()


@router.message(Command('start'))
async def start(message: types.Message) -> None:
    """Приветственное сообщение с инструкцией по работе с ботом"""
    user_name: str = message.from_user.full_name
    await message.answer(
        text=BotMessage.START.format(user_name),
        parse_mode=ParseMode.MARKDOWN
    )


@router.message(F.text)
async def send_promt(message: types.Message, db: Database) -> None:
    """Отправка промта с последующим получением ответа от GPT"""
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    tg_id: int = message.from_user.id
    username: str = message.from_user.username
    full_name: str = message.from_user.full_name
    text: str = message.text
    response: str = await get_answer(message.text)

    try:
        await message.answer(text=response)
    except Exception:
        await message.answer(text=BotMessage.PARSE_ERROR)

    await db.execute(
        Query.INSERT_MESSAGE, tg_id, username, full_name, text, response
    )

