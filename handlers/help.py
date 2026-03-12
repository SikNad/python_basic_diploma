from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def help_command(message: Message):
    """Показывает список доступных команд"""
    help_text = (
        "🎬 *Команды кино-бота:*\n\n"
        "🔍 /search <название> - поиск фильмов\n"
        "📽 /film <id> - детали фильма по ID\n"
        "📋 /history - история ваших запросов\n"
        "🎲 /random - случайный фильм (скоро)\n"
        "🔥 /trends - популярные фильмы (скоро)\n"
        "🌟 /upcoming - ожидаемые новинки (скоро)\n\n"
        "👋 /hello-world - приветствие\n"
        "❓ /help - это сообщение"
    )

    bot.reply_to(message, help_text, parse_mode='Markdown')
