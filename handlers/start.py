from loader import bot
from telebot.types import Message
from database.user_service import get_or_create_user


@bot.message_handler(commands=['start'])
def start_command(message: Message):
    """Обработчик команды /start - первая точка входа"""
    user = get_or_create_user(message)

    welcome_text = (
        f"🎬 Привет, {message.from_user.first_name}!\n\n"
        "Я бот для поиска фильмов. Вот что я умею:\n\n"
        "🔍 /search <название> - найти фильм\n"
        "📜 /history - показать историю поиска\n"
        "❓ /help - помощь\n\n"
        "Попробуй прямо сейчас: /search Матрица"
    )
    bot.reply_to(message, welcome_text)


@bot.message_handler(commands=['hello-world'])
def hello_world_command(message: Message):
    """Обработчик команды /hello-world"""
    user = get_or_create_user(message)
    bot.reply_to(
        message,
        "🌟 Привет, мир! Я бот для поиска фильмов. Используй /help для списка команд."
    )


@bot.message_handler(commands=['help'])
def help_command(message: Message):
    """Обработчик команды /help"""
    user = get_or_create_user(message)

    help_text = (
        "📖 *Доступные команды:*\n\n"
        "/start - Начать работу с ботом\n"
        "/search <название> - Поиск фильма\n"
        "/history - История ваших поисков\n"
        "/hello-world - Тестовая команда\n"
        "/help - Эта справка\n"
        "/donate - Поддержать разработчика\n\n"
        "📝 *Пример:* `/search Матрица`"
    )
    bot.reply_to(message, help_text, parse_mode='Markdown')


@bot.message_handler(commands=['donate'])
def donate_command(message: Message):
    """Обработчик команды /donate - поддержать разработчика"""
    donate_url = "https://donate.stream/yoomoney4100119521365903"
    donate_text = (
        "☕️ **Поддержать разработчика**\n\n"
        "Если вам нравится бот и вы хотите помочь его развитию, "
        "вы можете отправить донат по ссылке ниже:\n\n"
        f"[Отправить донат]({donate_url})\n\n"
        "Спасибо за поддержку! 💖"
    )
    bot.send_message(message.chat.id, donate_text, parse_mode='Markdown')


@bot.message_handler(func=lambda message: message.text.lower() == 'привет')
def hello_text(message: Message):
    """Обработчик текста 'Привет'"""
    user = get_or_create_user(message)

    welcome_text = (
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Я бот для поиска фильмов. Вот что я умею:\n\n"
        "🔍 /search <название> - найти фильм\n"
        "📜 /history - показать историю поиска\n"
        "❓ /help - помощь\n\n"
        "Попробуй прямо сейчас: /search Матрица"
    )
    bot.reply_to(message, welcome_text)
