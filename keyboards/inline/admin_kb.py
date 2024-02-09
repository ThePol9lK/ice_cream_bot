from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def template_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура выбора шаблонов
    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    template_dict = {
        "Категория": "category",
        "Товар": "product"
    }

    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=button,
                    callback_data=template_dict[button]
                )
            ] for button in template_dict
        ]
    )


def action_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура для выбора действия
    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    action_dict = {
        "Добавить": "add",
        "Удалить": "delete",
        "Изменить": "change"
    }

    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=button,
                    callback_data=action_dict[button]
                )
            ] for button in action_dict
        ]
    )
