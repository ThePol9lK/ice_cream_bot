from telebot.handler_backends import State, StatesGroup


class Feedback(StatesGroup):
    """Класс с состояниями бота"""

    commit = State()
    email = State()
    feedback = State()
