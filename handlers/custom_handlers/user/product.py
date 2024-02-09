import json
from loader import bot
from telebot.types import Message, CallbackQuery, InputMediaPhoto

from database.CRUD import get_product_brands
from states.user_states.user_product_state import UserProduct

from keyboards.inline.product_kb import all_brands_kb
from keyboards.inline.pagination_first import pagination_first
from keyboards.inline.pagination_last import pagination_last
from keyboards.inline.pagination_others import pagination_others


@bot.message_handler(commands=["catalog"])
def display_brands(message: Message):
    """
    Обработка команды catalog.

    :param message: Message
    :return:
    """
    bot.delete_state(message.from_user.id, message.chat.id)

    bot.send_message(message.chat.id, 'Выберите бренд товара', reply_markup=all_brands_kb())
    bot.set_state(message.chat.id, UserProduct.brand)


@bot.callback_query_handler(func=lambda call: True, state=UserProduct.brand)
def display_product(call: CallbackQuery):
    """
    Обработка вывода первого товара из категории брендов

    :param call: CallbackQuery
    :return:
    """
    all_collective = get_product_brands(int(call.data))
    img = open(all_collective[0].image, 'rb')

    bot.send_photo(chat_id=call.message.chat.id,
                   photo=img,
                   caption=f'{all_collective[0].name}\n{all_collective[0].description}',
                   reply_markup=pagination_first(
                       count=len(all_collective),
                       page=0,
                       key='product',
                       link=all_collective[0].link,
                       key_2=call.data,
                   )
                   )
    bot.set_state(call.from_user.id, UserProduct.product, call.message.chat.id)




@bot.callback_query_handler(func=lambda call: call.data.startswith('{"KeyPage":"product"'), state=UserProduct.product,)
def callback_query_pagination(call: CallbackQuery) -> None:
    """
    Обработка пагинации на команду catalog

    :param call: CallbackQuery
    :return:
    """
    json_string = json.loads(call.data)
    count = json_string['NumberPage']
    key = json_string['KeyPage']
    key_2 = json_string['Key']

    all_collective = get_product_brands(int(key_2))
    poster_photo = open(all_collective[count].image, 'rb')
    caption = f'{all_collective[count].name}\n{all_collective[count].description}'
    link = all_collective[count].link

    media = InputMediaPhoto(poster_photo, caption=caption)

    if count == 0:
        keyboard = pagination_first(
            count=len(all_collective),
            page=count,
            key=key,
            link=link,
            key_2=key_2
        )

    elif count == len(all_collective) - 1:
        keyboard = pagination_last(
            count=len(all_collective),
            page=count,
            key=key,
            link=link,
            key_2=key_2
        )

    else:
        keyboard = pagination_others(
            count=len(all_collective),
            page=count,
            key=key,
            link=link,
            key_2=key_2
        )

    bot.edit_message_media(media=media,
                           chat_id=call.message.chat.id,
                           message_id=call.message.message_id,
                           reply_markup=keyboard)