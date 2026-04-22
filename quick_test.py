
import telebot
import urllib.request

print("=" * 50)
print("🔍 БЫСТРАЯ ПРОВЕРКА БОТА")
print("=" * 50)

# ТОКЕН ИЗ .ENV
TOKEN = "8601470478:AAEsIAJo-a9YX3mbaZWo5E7Z0L6YzjHprJE"

print(f"1. Проверяем доступ к API...")
try:
    urllib.request.urlopen("https://api.telegram.org", timeout=5)
    print("   ✅ Telegram API доступен")
except Exception as e:
    print(f"   ❌ Ошибка: {e}")
    exit()

print(f"\n2. Проверяем бота...")
try:
    bot = telebot.TeleBot(TOKEN)
    me = bot.get_me()
    print(f"   ✅ Бот подключен!")
    print(f"   🆔 ID: {me.id}")
    print(f"   📝 Имя: {me.first_name}")
    print(f"   @{me.username}")
    print("\n" + "=" * 50)
    print("🎉 БОТ ГОТОВ К ЗАПУСКУ!")
    print("=" * 50)
    print("\nТеперь можете запускать:")
    print("python main.py")
except Exception as e:
    print(f"   ❌ Ошибка: {e}")
    print("\nВозможно, токен неправильный.")
    print("Проверьте токен в файле .env")
