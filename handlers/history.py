from loader import bot
from telebot.types import Message
from database.models import User, SearchHistory


@bot.message_handler(commands=['history'])
def show_history(message: Message):
    """Показать историю поиска пользователя"""
    try:
        # Находим пользователя
        try:
            user = User.get(User.user_id == message.from_user.id)
        except User.DoesNotExist:
            bot.reply_to(
                message,
                "📭 У вас пока нет истории поиска.\n"
                "Используйте /search <название фильма> для поиска."
            )
            return

        # Получаем историю
        history = SearchHistory.select().where(
            SearchHistory.user == user
        ).order_by(SearchHistory.created_at.desc()).limit(10)

        # Проверяем, есть ли записи
        if not history.exists():
            bot.reply_to(
                message,
                "📭 У вас пока нет истории поиска.\n"
                "Используйте /search <название фильма> для поиска."
            )
            return

        # Формируем сообщение
        text = "📜 *Ваша история поиска (последние 10):*\n\n"

        for item in history:
            results_count = len(item.get_results_list()) if item.results else 0
            text += f"• *{item.created_at.strftime('%d.%m.%Y %H:%M')}*\n"
            text += f"  🔍 *{item.command}:* `{item.query}`\n"
            text += f"  📊 Найдено: {results_count} фильмов\n\n"

        bot.send_message(
            message.chat.id,
            text,
            parse_mode='Markdown'
        )

    except Exception as e:
        print(f"❌ Ошибка при показе истории: {e}")
        bot.reply_to(
            message,
            "❌ Произошла ошибка при загрузке истории. Попробуйте позже."
        )
