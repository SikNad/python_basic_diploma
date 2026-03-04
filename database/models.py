from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField
from database.db import db
import datetime

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField(primary_key=True, unique=True)
    username = CharField(null=True)
    first_name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

def create_models():
    """Создание всех таблиц"""
    with db:
        db.create_tables([User])
        print("✅ Таблицы созданы успешно")
