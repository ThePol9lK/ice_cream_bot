from telebot.types import Message, CallbackQuery
from loader import bot

from keyboards.inline.admin_kb import template_kb, action_kb
from keyboards.inline.product_kb import all_brands_kb

from states.admin_states.admin import AdminState
from states.admin_states.category import AddCategoryState, DeleteCategoryState, UpdateCategoryState
from states.admin_states.product import AddProductState, DeleteProductState, UpdateProductState


@bot.message_handler(commands=["admin"])
def select_template(message: Message):
    """
    Обработка команды admin
    :param message:
    :return:
    """
    bot.send_message(message.from_user.id, "Выбери категорию из меню", reply_markup=template_kb())
    bot.set_state(message.from_user.id, AdminState.step_1, message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=AdminState.step_1)
def select_action(call: CallbackQuery):
    """
    Выбор категории или товара
    :param call:
    :return:
    """
    bot.set_state(call.from_user.id, AdminState.step_2, call.message.chat.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['template'] = call.data

    bot.send_message(call.from_user.id, "Выбери значение из меню", reply_markup=action_kb())


@bot.callback_query_handler(func=lambda call: call.data == 'add', state=AdminState.step_2)
def check_action(call: CallbackQuery):
    """
    Обработка добавления
    :param call:
    :return:
    """
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'category':
            bot.set_state(call.from_user.id, AddCategoryState.name, call.message.chat.id)
            bot.send_message(call.from_user.id, "Напиши имя категории")
        elif data['template'] == 'product':
            bot.set_state(call.from_user.id, AddProductState.name, call.message.chat.id)
            bot.send_message(call.from_user.id, "Напиши имя товара")


@bot.callback_query_handler(func=lambda call: call.data == 'delete', state=AdminState.step_2)
def check_action(call: CallbackQuery):
    """
    Обработка удаления
    :param call:
    :return:
    """
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'category':
            bot.set_state(call.from_user.id, DeleteCategoryState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери категорию для удаления", reply_markup=all_brands_kb())
        elif data['template'] == 'product':
            bot.set_state(call.from_user.id, DeleteProductState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери категорию товара для удаления", reply_markup=all_brands_kb())


@bot.callback_query_handler(func=lambda call: call.data == 'change', state=AdminState.step_2)
def check_action(call: CallbackQuery):
    """
    Обработка изменения
    :param call:
    :return:
    """
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'category':
            bot.set_state(call.from_user.id, UpdateCategoryState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери категорию для изменения", reply_markup=all_brands_kb())
        elif data['template'] == 'product':
            bot.set_state(call.from_user.id, UpdateProductState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери категорию товара для изменения", reply_markup=all_brands_kb())
