from g4f import ChatCompletion
import traceback


async def get_answer(promt: str) -> str:
    try:
        response = await ChatCompletion.create_async(
            model='gpt-4',
            messages=[{'role': 'user', 'content': promt}]
        )
    except Exception:
        try:
            response = await ChatCompletion.create_async(
                model='gpt-3.5-turbo',
                messages=[{'role': 'user', 'content': promt}]
            )
        except Exception:
            response = traceback.format_exc()

    return response
