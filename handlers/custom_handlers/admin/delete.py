from telebot.types import CallbackQuery
from loader import bot

from database.CRUD import delete_brand, delete_product
from keyboards.inline.product_kb import all_product_kb

from states.admin_states.category import DeleteCategoryState
from states.admin_states.product import DeleteProductState


@bot.callback_query_handler(func=lambda call: True, state=DeleteCategoryState.choice)
def delete_category(call: CallbackQuery):
    """
    Удаление категории товаров
    :param call:
    :return:
    """
    bot.delete_state(call.from_user.id, call.message.chat.id)
    delete_brand(int(call.data))
    bot.send_message(call.from_user.id, "Категория удалена")


@bot.callback_query_handler(func=lambda call: True, state=DeleteProductState.choice)
def choice_category(call: CallbackQuery):
    """
    Выбор категории товаров
    :param call:
    :return:
    """
    bot.send_message(call.from_user.id, "Выбери товар из категории", reply_markup=all_product_kb(int(call.data)))
    bot.set_state(call.from_user.id, DeleteProductState.choice_product, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=DeleteProductState.choice_product)
def delete_prod(call: CallbackQuery):
    """
    Удаление товара
    :param call:
    :return:
    """
    bot.delete_state(call.from_user.id, call.message.chat.id)
    delete_product(int(call.data))
    bot.send_message(call.from_user.id, "Товар удален")
