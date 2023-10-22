from telebot.handler_backends import State, StatesGroup


class UserProduct(StatesGroup):
    """Класс с состояниями бота"""

    brand = State()
    product = State()
