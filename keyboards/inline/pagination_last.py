from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def pagination_last(count: int, page: int, key: str, key_2: str = None, link: str = None, link_second: str = None) -> InlineKeyboardMarkup:
    """
    Клавиатура пагинация для вывода фото (на последнее фото)

    :param count:
    :param page:
    :param key:
    :param link:
    :param link_second:
    :return:
    """

    markup = InlineKeyboardMarkup()

    if key_2:
        markup.add(
            InlineKeyboardButton(text=f'Предыдущее',
                                 callback_data="{\"KeyPage\":" + '"' + key + '"' + ",\"NumberPage\":" + str(
                                     page - 1) + ",\"Key\":" + str(key_2) +"}"
                                 ),

            InlineKeyboardButton(text=f'{page + 1}/{count}',
                                 callback_data=f' ')
        )
    else:
        markup.add(
            InlineKeyboardButton(text=f'Предыдущее',
                                 callback_data="{\"KeyPage\":" + '"' + key + '"' + ",\"NumberPage\":" + str(
                                     page - 1) + "}"
                                 ),

            InlineKeyboardButton(text=f'{page + 1}/{count}',
                                 callback_data=f' ')
        )

    if link:
        markup.add(InlineKeyboardButton(text='Больше информации', url=f'{link}'))

    if link_second:
        markup.add(InlineKeyboardButton(text='Купить билет', url=f'{link_second}'))

    return markup
