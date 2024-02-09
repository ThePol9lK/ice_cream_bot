from telebot.types import Message, CallbackQuery

from database.CRUD import add_brand, add_product
from loader import bot

from keyboards.inline.product_kb import all_brands_kb

from states.admin_states.category import AddCategoryState
from states.admin_states.product import AddProductState


# Добавление категории
@bot.message_handler(state=AddCategoryState.name)
def add_name_category(message: Message):
    """
    Добавление новой категории товаров
    :param message:
    :return:
    """
    add_brand(message.text)
    bot.send_message(message.from_user.id, 'Категория успешно добавлена')
    bot.delete_state(message.from_user.id, message.chat.id)


# Добавление товара
@bot.message_handler(state=AddProductState.name)
def add_name_product(message: Message):
    """
    Добавление имени товара
    :param message:
    :return:
    """
    bot.send_message(message.from_user.id, "Напиши описание продукта")
    bot.set_state(message.from_user.id, AddProductState.description, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['name'] = message.text


@bot.message_handler(state=AddProductState.description)
def add_description_product(message: Message):
    """
    Добавление описания товароа
    :param message:
    :return:
    """
    bot.send_message(message.from_user.id, "Напиши ссылку продукта")
    bot.set_state(message.from_user.id, AddProductState.link, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['description'] = message.text


@bot.message_handler(state=AddProductState.link)
def add_link_product(message: Message):
    """
    Добавление ссылки товара
    :param message:
    :return:
    """
    bot.send_message(message.from_user.id, "Выбери категорию для товара", reply_markup=all_brands_kb())
    bot.set_state(message.from_user.id, AddProductState.id_category, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['link'] = message.text


@bot.callback_query_handler(func=lambda call: True, state=AddProductState.id_category)
def add_id_category_product(call: CallbackQuery):
    """
    Добавление категории товара
    :param message:
    :return:
    """
    bot.send_message(call.from_user.id, "Пришли фото продукта")
    bot.set_state(call.from_user.id, AddProductState.image, call.message.chat.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_category'] = int(call.data)


@bot.message_handler(state=AddProductState.image, content_types=['photo'])
def add_photo_product(message: Message):
    """
    Добавление товара
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
                 'id_category': add_data['id_category']}
        add_product(param)

    bot.send_message(message.from_user.id, "Новый товар добавлен")
    bot.delete_state(message.from_user.id, message.chat.id)
