from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField
from database.db import db
import datetime


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    """Модель пользователя"""
    user_id = IntegerField(primary_key=True, unique=True)
    username = CharField(null=True)
    first_name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)


class SearchHistory(BaseModel):
    """Модель истории поиска фильмов"""
    user = ForeignKeyField(User, backref='searches')  # связь с пользователем
    query = CharField()  # поисковый запрос
    movie_title = CharField(null=True)  # название выбранного фильма
    movie_year = IntegerField(null=True)  # год фильма
    rating = CharField(null=True)  # рейтинг (строка, чтобы сохранять как есть)
    searched_at = DateTimeField(default=datetime.datetime.now)  # время поиска


def create_models():
    """Создание всех таблиц в базе данных"""
    with db:
        db.create_tables([User, SearchHistory])
        print("✅ Таблицы User и SearchHistory созданы успешно")
