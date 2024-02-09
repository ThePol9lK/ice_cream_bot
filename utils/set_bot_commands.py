from telebot.types import BotCommand
from config_data.config import COMMANDS


def set_default_commands(bot) -> None:
    """
    Задаем команды для бота

    :param bot: Bot
    :return:
    """
    bot.set_my_commands(
        [BotCommand(*i) for i in COMMANDS]
    )
