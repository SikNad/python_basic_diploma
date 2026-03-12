from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, TextField
from database.db import db
import datetime
import json


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True, unique=True)
    username = CharField(null=True)
    first_name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)


# НОВАЯ МОДЕЛЬ ДЛЯ ИСТОРИИ ПОИСКА
class SearchHistory(BaseModel):
    user = ForeignKeyField(User, backref='searches')
    command = CharField()  # какая команда (/search, /rating, /low_budget)
    query = CharField()  # поисковый запрос
    results = TextField()  # результаты (JSON строка)
    created_at = DateTimeField(default=datetime.datetime.now)

    def get_results_list(self):
        """Преобразует JSON строку обратно в список"""
        return json.loads(self.results) if self.results else []

    def __str__(self):
        # Форматируем строку для вывода в истории
        results_count = len(self.get_results_list()) if self.results else 0
        return f"{self.created_at.strftime('%d.%m.%Y %H:%M')} - {self.command}: '{self.query}' (найдено: {results_count})"


def create_models():
    """Создание всех таблиц"""
    with db:
        db.create_tables([User, SearchHistory])
        print("✅ Таблицы созданы успешно")
