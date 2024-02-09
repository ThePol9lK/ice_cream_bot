import peewee
from .models import db, Brand, Product


def get_all_brands() -> peewee.ModelSelect:
    """
    Вывод всех значений брендов

    :return: peewee.ModelSelect
    """
    return Brand.select()


def add_brand(title: str) -> None:
    """
    Добавление категории

    :param title: str
    :return:
    """
    Brand.insert({Brand.title: title}).execute()


def update_brand(title: str, id_brand: int) -> None:
    """
    Обновление категории

    :param id_brand:
    :param title: str
    :return:
    """
    Brand.update(title=title).where(Brand.id == id_brand).execute()


def delete_brand(id_brand: int) -> None:
    """
    Удаление категории

    :param id_brand:
    :return:
    """
    Brand.delete().where(Brand.id == id_brand).execute()


def get_product_brands(id_brand: int) -> peewee.ModelSelect:
    """
    Вывод всех товаров по бренду

    :return: peewee.ModelSelect
    """
    return Product.select().where(Product.category == id_brand)


def get_product(id_product: int) -> peewee.ModelSelect:
    """
    Вывод товара по id

    :return: peewee.ModelSelect
    """
    return Product.select().where(Product.id == id_product)


def delete_product(id_product: int) -> None:
    """
    Удаление товара

    :param id_product:
    :return:
    """
    Product.delete().where(Product.id == id_product).execute()


def add_product(params: dict) -> None:
    """
    Добавление товара

    :param params:
    :return:
    """
    Product.insert({Product.name: params['name'],
                    Product.description: params['description'],
                    Product.image: params['image'],
                    Product.link: params['link'],
                    Product.category: params['id_category']}).execute()


def update_product(params: dict) -> None:
    """
    Обновление категории

    :param params:
    :return:
    """
    Product.update({Product.name: params['name'],
                    Product.description: params['description'],
                    Product.image: params['image'],
                    Product.link: params['link'],
                    Product.category: params['id_category']}).where(Product.id == params['id_product']).execute()


def create_tables() -> None:
    """
    Создание таблиц для базы данных

    :return:
    """
    with db:
        db.create_tables([Brand, Product])


db.connect()
create_tables()
