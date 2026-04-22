import telebot
from telebot import apihelper
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

# Увеличиваем таймауты
apihelper.CONNECT_TIMEOUT = 30
apihelper.READ_TIMEOUT = 30

# НАСТРОЙКА ПРОКСИ (если нужна)
# Раскомментируйте и укажите ваши настройки прокси

# Для HTTP/HTTPS прокси:
# apihelper.proxy = {
#     'http': 'http://ваш_прокси:порт',
#     'https': 'http://ваш_прокси:порт'
# }

# Для SOCKS5 прокси (нужна библиотека: pip install pysocks):
# apihelper.proxy = {
#     'http': 'socks5://ваш_прокси:порт',
#     'https': 'socks5://ваш_прокси:порт'
# }

# Если Telegram API заблокирован, можно попробовать изменить URL
# telebot.apihelper.API_URL = "https://api.telegram.org/bot{0}/{1}"

# Токен бота
TOKEN = "ВАШ_ТОКЕН_БОТА"

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Проверка подключения
def check_bot_connection():
    """Проверка подключения к Telegram API"""
    try:
        bot_info = bot.get_me()
        print("=" * 50)
        print("✅ БОТ УСПЕШНО ПОДКЛЮЧЕН!")
        print(f"   👤 Имя: {bot_info.first_name}")
        print(f"   🔖 Username: @{bot_info.username}")
        print(f"   🆔 ID: {bot_info.id}")
        print("=" * 50)
        return True
    except Exception as e:
        print("=" * 50)
        print("❌ ОШИБКА ПОДКЛЮЧЕНИЯ К TELEGRAM API")
        print(f"   📍 Ошибка: {e}")
        print(f"   📍 Тип: {type(e).__name__}")
        print("\n   🔧 ПРОВЕРЬТЕ:")
        print("   1. Интернет-соединение")
        print("   2. Правильность токена")
        print("   3. Доступность api.telegram.org")
        print("   4. Настройки прокси (если используются)")
        print("=" * 50)
        return False

# Выполняем проверку при загрузке
if __name__ != "__main__":
    check_bot_connection()
