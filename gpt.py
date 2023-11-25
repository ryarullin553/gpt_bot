from g4f import ChatCompletion
from constants import BotMessage


async def get_answer(promt: str) -> str:
    try:
        response = await ChatCompletion.create_async(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': promt}]
        )
        return response
    except Exception:
        return BotMessage.GPT_ERROR
