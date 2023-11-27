import copy
import random

from aiogram import Router, F, types
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import flags

from constants import BotMessage, Query, OVA_EMPLOYEES
from database import Database
from gpt import get_answer
from aiogram.fsm.context import FSMContext
from states import Gen

router = Router()


@router.message(Command('start'))
async def start(message: types.Message, state: FSMContext) -> None:
    """Приветственное сообщение с инструкцией по работе с ботом"""
    await state.clear()
    user_name: str = message.from_user.full_name
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text='Тайный Санта 🎁',
            callback_data='secret_santa'
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text='GPT 🤖',
            callback_data='gpt'
        )
    )
    await message.answer(
        text=BotMessage.START.format(user_name),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=builder.as_markup(),
        resize_keyboard=True
    )


@router.callback_query(F.data == 'gpt')
async def input_promt(callback: types.CallbackQuery,
                      state: FSMContext) -> None:
    """Включение режима часа с GPT"""
    await state.set_state(Gen.gpt_gen)
    await callback.message.answer(text='GPT mode')


@router.message(Gen.gpt_gen)
@flags.chat_action('typing')
async def send_promt(message: types.Message, db: Database) -> None:
    """Отправка промта с последующим получением ответа от GPT"""
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    tg_id: int = message.from_user.id
    username: str = message.from_user.username
    full_name: str = message.from_user.full_name
    text: str = message.text
    response: str = await get_answer(message.text)

    #try:
    await message.answer(text=response)
    # except Exception:
    #     await message.answer(text=BotMessage.PARSE_ERROR)

    await db.execute(
        Query.INSERT_MESSAGE, tg_id, username, full_name, text, response
    )


@router.callback_query(F.data == 'secret_santa')
async def secret_santa(callback: types.CallbackQuery,
                       state: FSMContext,
                       players: list[dict]):
    """Включение режима для Тайного Санты"""
    await state.set_state(Gen.santa_gen)
    username: str = callback.from_user.username
    username_players = [p['username'] for p in players]
    if username in OVA_EMPLOYEES and username not in username_players:
        await callback.message.answer(text=BotMessage.SECRET_SANTA)
    else:
        await callback.message.answer(text=BotMessage.OVA_ERROR)


@router.message(Gen.santa_gen)
async def send_random_value(message: types.Message, players: list[dict], bot):
    """Регистрация участников игры"""
    username: str = message.from_user.username
    full_name: str = message.from_user.full_name
    text: str = message.text
    chat_id: int = message.chat.id
    username_players = [p['username'] for p in players]
    if username not in username_players:
        players.append({'username': username,
                        'full_name': full_name,
                        'text': text,
                        'chat_id': chat_id,
                        'to_user': None})
        await message.answer(text=BotMessage.JOINED)

        if len(players) == 9:
            vk = [p for p in players if p['username'] == 'madamkyl']
            employees = copy.deepcopy([p for p in players if p['username'] != 'madamkyl'])
            for player in players:
                while True:
                    rand_int = random.randint(0, len(employees) - 1)
                    employee = employees[rand_int]
                    if employee['username'] != player['username']:
                        break
                if player['username'] == 'vita_vacua':
                    player['to_user'] = vk[0]['username']
                    await bot.send_message(
                        player['chat_id'],
                        text=BotMessage.RESULT_SANTA.format(
                            vk[0]['username'],
                            vk[0]['fullname'],
                            vk[0]['text']
                        )
                    )
                else:
                    employee = employees.pop(rand_int)
                    player['to_user'] = employee['username']
                    await bot.send_message(
                        player['chat_id'],
                        text=BotMessage.RESULT_SANTA.format(
                            employee['username'],
                            employee['fullname'],
                            employee['text']
                        )
                    )
    else:
        await message.answer(text=BotMessage.OVA_ERROR)


@router.message(Command('check'))
async def send_random_value(message: types.Message, players: list[dict]):
    """Просмотр список участников"""
    username: str = message.from_user.username
    answer = '\n'.join(str(el) for el in players)
    if username == 'vita_vacua' and players:
        await message.answer(text=answer)
