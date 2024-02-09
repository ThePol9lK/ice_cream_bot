from telebot.types import Message
from loader import bot


@bot.message_handler(commands=["contacts"])
def display_contacts(message: Message):
    """
    Функция для вывода информации о контактах ЦДК 'Созвездие'

    :param message: Message
    :return:
    """
    bot.send_message(message.chat.id,
                     '<b>Директор по продажам:</b> Беседин Денис Александрович\nDenis.Besedin@iceberry.ru\n\n'
                     '<b>Начальник Управления Продаж Москвы:</b> Сидорков Николай Александрович\n<a href="+79163431887">+79163431887</a>\nNikolay.Sidorkov@iceberry.ru\n\n'
                     '<b>Начальник Управления Продаж МО:</b>Бычкин Матвей Вячеславович Моб.\n <a href="+79161059159">+79161059159</a>\nMatvey.Bychkin@iceberry.ru\n\n'
                     '<b>Колл-центр для заказа мороженого в Москве и МО</b>\n <a href="+79150426740">+79150426740</a>',
                     parse_mode="HTML"
                     )
