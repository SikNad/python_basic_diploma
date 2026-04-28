
from loader import bot
from database.models import create_models
import handlers.start
import handlers.search
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

# Фейковый веб-сервер для Render (чтобы не падал с ошибкой "No open ports")
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running!')

def run_web():
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    server.serve_forever()

# Запускаем веб-сервер в отдельном потоке
Thread(target=run_web, daemon=True).start()

if __name__ == "__main__":
    print("🚀 Инициализация базы данных...")
    create_models()
    print("✅ База данных готова!")
    print("🤖 Бот запущен. Нажми Ctrl+C для остановки.")
    print("📝 Доступные команды: /start, /search <название>, /history, /help, /donate")

    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print("👋 Бот остановлен")
