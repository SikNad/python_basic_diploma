from loader import bot
from database.models import create_models

# Импортируем все обработчики
import handlers.start
import handlers.help
import handlers.search  # 👈 ЭТА СТРОКА ДОЛЖНА БЫТЬ!
import handlers.history

if __name__ == "__main__":
    print("🔒 Инициализация базы данных...")
    create_models()
    print("📂 База данных готова!")
    print("💡 Бот запущен. Нажми Ctrl+C для остановки.")
    print("Доступные команды: /hello-world, /search, /film, /history, /help")

    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print("👋 Бот остановлен")
