

class BotMessage:
    START = "Приветствую, *{}*! Я бесплатный ChatGPT бот 🤖\n" \
            "Пиши мне вопросы и я постараюсь на них ответить."
    GPT_ERROR = "Провайдер недоступен 😭."
    PARSE_ERROR = "Некорректный ответ от GPT. Попробуйте еще раз"


class Query:
    INSERT_MESSAGE = '''
        INSERT INTO MESSAGES (TG_ID, USERNAME, FULL_NAME, TEXT, RESPONSE)
        VALUES ($1, $2, $3, $4, $5)
    '''
