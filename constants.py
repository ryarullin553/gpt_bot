

class BotMessage:
    START = "Приветствую, *{}*! Я бесплатный ChatGPT бот 🤖\n" \
            "Пиши мне вопросы и я постараюсь на них ответить."
    GPT_ERROR = "Провайдер недоступен 😭."
    PARSE_ERROR = "Некорректный ответ от GPT. Попробуйте еще раз"
    SECRET_SANTA = "Чтобы упростить задачу человеку, который будет дарить вам " \
                   "подарок, можете написать что примерно вы желаете получить. " \
                   "Например _'что-то шоколадное'_ или _'что-то из денег'_. " \
                   "Учтите, что ваше пожелание может быть проигнорировано."
    OVA_ERROR = "Вы уже зарегистрировались или не являетесь сотрудником ОВА"
    JOINED = "Вы приняли участие 🎉 \n" \
             "Как только зарегистрируются все сотрудники ОВА, " \
             "вам придет сообщение с информацией, кому вы должны сделать подарок."
    RESULT_SANTA = "Вам необходимо будет сделать подарок @{}.\n" \
                   "У {} следующие пожелания: *{}*"


class Query:
    INSERT_MESSAGE = '''
        INSERT INTO MESSAGES (TG_ID, USERNAME, FULL_NAME, TEXT, RESPONSE)
        VALUES ($1, $2, $3, $4, $5)
    '''
    INSERT_SANTA = '''
        INSERT INTO SANTA (PLAYER, EMPLOYEE, TEXT)
        VALUES ($1, $2, $3)
    '''


OVA_EMPLOYEES = [
                 'vita_vacua',
                 'IskanderFatkhullin',
                 'kinzyaaa',
                 'rezzzyy',
                 'Linar24',
                 'Raslman',
                 'blackst0ne1',
                 'madamkyl',
                 'furya42'
                ]
