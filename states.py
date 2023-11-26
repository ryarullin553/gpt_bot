from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    gpt_gen = State()
    santa_gen = State()
