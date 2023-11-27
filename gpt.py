from g4f import ChatCompletion, Provider
from constants import BotMessage


async def get_answer(promt: str) -> str:
    try:
        response = await ChatCompletion.create_async(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': promt}],
            provider=Provider.GptForLove
        )
    except Exception:
        response = BotMessage.GPT_ERROR

    return response
