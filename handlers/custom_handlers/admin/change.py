from telebot.types import CallbackQuery, Message

from database.CRUD import update_brand, update_product
from keyboards.inline.product_kb import all_brands_kb, all_product_kb
from loader import bot

from states.admin_states.category import UpdateCategoryState
from states.admin_states.product import UpdateProductState


# Изменение категории
@bot.callback_query_handler(func=lambda call: True, state=UpdateCategoryState.choice)
def choice_category(call: CallbackQuery):
    """
    Выбор категории товаров
    :param call:
    :return:
    """
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_category'] = int(call.data)
    bot.send_message(call.from_user.id, "Напиши новое название")
    bot.set_state(call.from_user.id, UpdateCategoryState.name, call.message.chat.id)


@bot.message_handler(state=UpdateCategoryState.name)
def update_name_category(message: Message):
    """
    Изменение категории товаров
    :param message:
    :return:
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        update_brand(title=message.text, id_brand=add_data['id_category'])
    bot.send_message(message.from_user.id, 'Категория успешно обновлена')
    bot.delete_state(message.from_user.id, message.chat.id)


# Изменение товара
@bot.callback_query_handler(func=lambda call: True, state=UpdateProductState.choice)
def choice_category(call: CallbackQuery):
    """
    Выбор категории товаров
    :param call:
    :return:
    """
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_category'] = int(call.data)
    bot.send_message(call.from_user.id, "Выбери товар из категории", reply_markup=all_product_kb(int(call.data)))
    bot.set_state(call.from_user.id, UpdateProductState.choice_pr, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=UpdateProductState.choice_pr)
def update_id_product(call: CallbackQuery):
    """
    Выбор id товара
    :param message:
    :return:
    """
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_product'] = int(call.data)
    bot.send_message(call.from_user.id, "Напиши имя продукта")
    bot.set_state(call.from_user.id, UpdateProductState.name, call.message.chat.id)


@bot.message_handler(state=UpdateProductState.name)
def update_name_product(message: Message):
    """
    Изменение имени товара
    :param message:
    :return:
    """
    bot.send_message(message.from_user.id, "Напиши описание продукта")
    bot.set_state(message.from_user.id, UpdateProductState.description, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['name'] = message.text


@bot.message_handler(state=UpdateProductState.description)
def update_description_product(message: Message):
    """
    Изменение описание товара
    :param message:
    :return:
    """
    bot.send_message(message.from_user.id, "Напиши ссылку на продукт")
    bot.set_state(message.from_user.id, UpdateProductState.link, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['description'] = message.text


@bot.message_handler(state=UpdateProductState.link)
def update_link_product(message: Message):
    """
    Изменение ссылки товара
    :param call:
    :return:
    """
    bot.send_message(message.from_user.id, "Пришли фото продукта")
    bot.set_state(message.from_user.id, UpdateProductState.image, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['link'] = message.text


@bot.message_handler(state=UpdateProductState.image, content_types=['photo'])
def add_photo_product(message: Message):
    """
    Изменение товара
    :param message:
    :return:
    """
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = f'.\image\{photo.file_id}.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        param = {'name': add_data['name'],
                 'description': add_data['description'],
                 'link': add_data['link'],
                 'image': save_path,
                 'id_category': add_data['id_category'],
                 'id_product': add_data['id_product']}
        update_product(param)

    bot.send_message(message.from_user.id, "Товар успешно обновлен")
    bot.delete_state(message.from_user.id, message.chat.id)
