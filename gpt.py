from g4f import ChatCompletion


async def get_answer(promt: str) -> str:
    response = await ChatCompletion.create_async(
        model='gpt-4',
        messages=[{'role': 'user', 'content': promt}]
    )
    return response
