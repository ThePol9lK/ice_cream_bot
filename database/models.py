import peewee

db = peewee.SqliteDatabase('bot.db')


class ModelBase(peewee.Model):
    """
    Базовый класс для таблиц

    id:AutoField() - для таблицы
    """
    id = peewee.AutoField()

    class Meta:
        database = db


class Brand(ModelBase):
    """
    Таблица Бренд

    title:CharField() - имя бренда
    description:TextField() - описание афиши
    """
    title = peewee.CharField()



class Product(ModelBase):
    """
    Таблица Продуктов

    name:CharField()- имя продукта
    description:CharField() - описание продукта
    image:CharField() - фото продукта
    link:CharField() - адрес на сайте для учителя
    category:ForeignKeyField() - присоединение к брендам
    """
    name = peewee.CharField()
    description = peewee.CharField()
    image = peewee.CharField()
    link = peewee.CharField()
    category = peewee.ForeignKeyField(Brand)
