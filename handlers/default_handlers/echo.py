from telebot.types import Message
from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message) -> None:
    """
    Функция для отлова эхо состояния

    :param message: Message
    :return:
    """
    bot.reply_to(
        message, "Не могу понять тебя\nИспользуй команду /help"
    )
