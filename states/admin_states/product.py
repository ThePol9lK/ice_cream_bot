from telebot.handler_backends import State, StatesGroup


class AddProductState(StatesGroup):
    """Класс с состояниями бота"""

    name = State()
    description = State()
    image = State()
    id_category = State()
    link = State()


class DeleteProductState(StatesGroup):
    """Класс с состояниями бота"""

    choice = State()
    choice_product = State()


class UpdateProductState(StatesGroup):
    """Класс с состояниями бота"""
    choice = State()
    choice_pr = State()
    name = State()
    description = State()
    image = State()
    link = State()
