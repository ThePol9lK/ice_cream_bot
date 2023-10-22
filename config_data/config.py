import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():  # поиск env файла
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()  # загрузка env файла

BOT_TOKEN = os.getenv("BOT_TOKEN")
EMAIL = os.getenv("EMAIL")
PASSWORD_EMAIL = os.getenv("PASSWORD_EMAIL")

# Команды для бота
COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("anketa", "Обратная связь"),
    ("catalog", "Вывести товары"),
    ("contacts", "Вывод информации о магазине")
)
