from loader import bot
from telebot.types import Message
from database.models import SearchHistory, User
from keyboards.reply import get_main_keyboard
import json


@bot.message_handler(commands=['history'])
def history_command(message: Message):
    """Показать историю поиска пользователя"""
    user_id = message.from_user.id

    # Получаем последние 10 записей истории
    history = (SearchHistory
               .select()
               .join(User)
               .where(User.user_id == user_id)
               .order_by(SearchHistory.created_at.desc())
               .limit(10))

    if not history:
        bot.send_message(
            message.chat.id,
            "📭 У вас пока нет истории поиска. Используйте команды поиска фильмов!",
            reply_markup=get_main_keyboard()
        )
        return

    # Формируем сообщение с историей
    text = "📋 *Ваша история поиска:*\n\n"

    for idx, record in enumerate(history, 1):
        text += f"{idx}. {record}\n"

    bot.send_message(
        message.chat.id,
        text,
        parse_mode='Markdown',
        reply_markup=get_main_keyboard()
    )


@bot.message_handler(func=lambda message: message.text == "📋 История поиска")
def history_button(message: Message):
    """Обработчик кнопки истории"""
    history_command(message)
