from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()  # создание машины состояний
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)  # создание бота
