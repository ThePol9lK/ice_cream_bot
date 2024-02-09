from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message) -> None:
    """
    Функция для запуска бота

    :param message: Message
    :return:
    """
    bot.reply_to(message, f"Привет, друг! Напиши /help для вывода информация что я могу.")
