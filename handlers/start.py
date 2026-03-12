from loader import bot
from telebot.types import Message
from database.models import User


@bot.message_handler(commands=['hello-world'])
def hello_world_command(message: Message):
    """Обработчик команды /hello-world"""
    bot.reply_to(
        message,
        "🌟 Привет, мир! Я бот для поиска фильмов. Используй /help для списка команд."
    )


@bot.message_handler(func=lambda message: message.text.lower() == 'привет')
def hello_text(message: Message):
    """Обработчик текста 'Привет'"""
    user_id = message.from_user.id

    # Сохраняем пользователя в БД
    user, created = User.get_or_create(
        user_id=user_id,
        defaults={
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        }
    )

    welcome_text = (
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Я бот для поиска фильмов. В будущем я научусь:\n"
        "• Искать фильмы по названию\n"
        "• Искать по рейтингу\n"
        "• Искать по бюджету\n"
        "• Хранить историю запросов\n\n"
        "А пока я понимаю только /hello-world и 'Привет'"
    )

    bot.reply_to(message, welcome_text)
