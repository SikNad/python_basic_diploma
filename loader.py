import telebot
from telebot.storage import StateMemoryStorage
from telebot import apihelper
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Увеличиваем таймауты для подключения к Telegram API
apihelper.CONNECT_TIMEOUT = 30  # Таймаут подключения (секунды)
apihelper.READ_TIMEOUT = 30     # Таймаут чтения (секунды)

# Токен бота
BOT_TOKEN = "8601470478:AAEsIAJo-a9YX3mbazWo5E7ZOL6YzjHprJE"

# Хранилище состояний
state_storage = StateMemoryStorage()

# Создаем экземпляр бота
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

# Проверка подключения к Telegram API
try:
    bot_info = bot.get_me()
    print("=" * 50)
    print("✅ БОТ УСПЕШНО ПОДКЛЮЧЕН!")
    print(f"   👤 Имя: {bot_info.first_name}")
    print(f"   🔖 Username: @{bot_info.username}")
    print(f"   🆔 ID: {bot_info.id}")
    print("=" * 50)
except Exception as e:
    print("=" * 50)
    print("❌ ОШИБКА ПОДКЛЮЧЕНИЯ К TELEGRAM API")
    print(f"   📍 Ошибка: {e}")
    print(f"   📍 Тип: {type(e).__name__}")
    print("\n   🔧 ПРОВЕРЬТЕ:")
    print("   1. Интернет-соединение")
    print("   2. Доступность api.telegram.org")
    print("   3. Включен ли VPN (если Telegram заблокирован)")
    print("=" * 50)
