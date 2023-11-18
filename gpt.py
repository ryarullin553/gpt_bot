from g4f import ChatCompletion, Provider


async def get_answer(promt: str) -> str:
    response = await ChatCompletion.create_async(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': promt}],
        provider=Provider.GPTalk,
    )
    return response
