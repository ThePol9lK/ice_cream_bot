import smtplib
from email.mime.text import MIMEText

from telebot.types import Message
from config_data.config import EMAIL, PASSWORD_EMAIL
from loader import bot
from states.user_states.anketa_states import Feedback


@bot.message_handler(commands=["anketa"])
def getting_theme(message: Message):
    """
    Функция для обработки команды anketa. Сохраняет значения от пользователя и отправляет сообщение на почту.

    :param message: Message
    :return:
    """
    bot.delete_state(message.from_user.id, message.chat.id)

    bot.send_message(message.chat.id, "Напишите тему сообщения")
    bot.set_state(message.from_user.id, Feedback.commit)


@bot.message_handler(func=None, state=Feedback.commit)
def getting_comment(message: Message):
    """
    Сохранение значения темы сообщения. Отлавливается через состояние Feedback.commit.

    :param message: Message
    :return:
    """
    bot.set_state(message.from_user.id, Feedback.feedback)
    bot.send_message(message.chat.id, "Напишите комментарий или сообщение")
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["subject"] = message.text


@bot.message_handler(func=None, state=Feedback.feedback)
def send_email(message: Message):
    """
    Сохранение значения сообщения и отправляет на почту. Отлавливается через состояние Feedback.feedback.

    :param message: Message
    :return:
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        msg = MIMEText(f'Пользователь - {message.from_user.first_name} {message.from_user.last_name} написал '
                       f'следующий текст:\n{message.text}\nСообщение пришло из телеграмм бота.')
        msg['Subject'] = data["subject"]
        msg['From'] = 'telegram_bot'
        msg['To'] = EMAIL

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD_EMAIL)
            server.send_message(msg)

    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв 😃")
