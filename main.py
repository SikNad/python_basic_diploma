from loader import bot
from database.models import create_models
import handlers.start  # импортируем обработчики

if __name__ == "__main__":
    print("🚀 Инициализация базы данных...")
    create_models()
    print("✅ База данных готова!")
    print("🤖 Бот запущен. Нажми Ctrl+C для остановки.")
    print("📝 Тестовые команды: /hello-world, 'Привет'")

    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print("👋 Бот остановлен")
