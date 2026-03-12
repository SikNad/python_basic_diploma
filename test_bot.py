import os
from dotenv import load_dotenv
import telebot

load_dotenv()
token = os.getenv('BOT_TOKEN')

print("=" * 50)
print("ПРОВЕРКА ТОКЕНА БОТА")
print("=" * 50)

print(f"Токен из .env: '{token}'")
print(f"Длина токена: {len(token)} символов")
print(f"Первые 10 символов: {token[:10]}...")
print(f"Последние 10 символов: ...{token[-10:]}")

print("\n" + "=" * 50)
print("ПРОВЕРКА ПОДКЛЮЧЕНИЯ К TELEGRAM")
print("=" * 50)

try:
    bot = telebot.TeleBot(token)
    bot_info = bot.get_me()
    print("✅ УСПЕХ! Бот работает!")
    print(f"   Имя бота: {bot_info.first_name}")
    print(f"   Username: @{bot_info.username}")
    print(f"   ID: {bot_info.id}")
except Exception as e:
    print("❌ ОШИБКА!")
    print(f"   Тип ошибки: {type(e).__name__}")
    print(f"   Описание: {e}")

    if "401" in str(e):
        print("\n🔴 Проблема: Неверный токен!")
        print("   Решение: Получите новый токен у BotFather")
    elif "socket" in str(e).lower():
        print("\n🔴 Проблема: Нет подключения к интернету!")
    else:
        print("\n🔴 Неизвестная ошибка")

print("\n" + "=" * 50)
print("ПРОВЕРКА ФАЙЛА .ENV")
print("=" * 50)

# Проверим, есть ли другие переменные
api_key = os.getenv('API_KEY')
db_path = os.getenv('DB_PATH')

print(f"API_KEY: {'✅ есть' if api_key else '❌ нет'}")
print(f"DB_PATH: {db_path}")
