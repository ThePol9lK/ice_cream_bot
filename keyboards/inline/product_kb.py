from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.CRUD import get_all_brands, get_product_brands


def all_brands_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура для вывода клавиатуры с категориями коллективов

    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=cat.title,
                    callback_data=cat.id
                )
            ] for cat in get_all_brands()
        ]
    )


def all_product_kb(id_brand:int) -> InlineKeyboardMarkup:
    """
    Клавиатура для вывода клавиатуры с товарами

    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=cat.name,
                    callback_data=cat.id
                )
            ] for cat in get_product_brands(id_brand=id_brand)
        ]
    )
