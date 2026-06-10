from loader import bot
from telebot.types import Message
from telebot import types
from database.user_service import get_or_create_user
from database.history_service import save_search_history, get_user_history_formatted

# Локальная база фильмов (для тестирования без API)
LOCAL_MOVIES = {
    'матрица': [
        {'id': 1, 'title': 'Матрица', 'year': 1999, 'rating': 8.5,
         'description': 'Культовый фильм о реальности и выборе. Программист Томас Андерсон узнаёт, что мир вокруг него — симуляция.'},
        {'id': 2, 'title': 'Матрица: Перезагрузка', 'year': 2003, 'rating': 7.8,
         'description': 'Продолжение истории Нео. Система наносит ответный удар.'},
        {'id': 3, 'title': 'Матрица: Революция', 'year': 2003, 'rating': 7.5,
         'description': 'Финальная битва за Зион и судьбу человечества.'},
        {'id': 4, 'title': 'Матрица: Воскрешение', 'year': 2021, 'rating': 7.2,
         'description': 'Новая глава истории. Нео снова в матрице.'},
    ],
    'форсаж': [
        {'id': 5, 'title': 'Форсаж', 'year': 2001, 'rating': 7.2,
         'description': 'Уличные гонки и дружба. Полицейский внедряется в банду уличных гонщиков.'},
        {'id': 6, 'title': 'Форсаж 2', 'year': 2003, 'rating': 6.8,
         'description': 'Брайан О\'Коннер помогает полиции поймать преступника.'},
        {'id': 7, 'title': 'Форсаж 3: Токийский дрифт', 'year': 2006, 'rating': 7.0,
         'description': 'Шон Босуэлл осваивает искусство дрифта в Токио.'},
        {'id': 8, 'title': 'Форсаж 4', 'year': 2009, 'rating': 7.1,
         'description': 'Доминик и Брайан объединяются против общего врага.'},
        {'id': 9, 'title': 'Форсаж 5', 'year': 2011, 'rating': 7.6,
         'description': 'Команда собирается для последнего дела в Рио.'},
    ],
    'титаник': [
        {'id': 10, 'title': 'Титаник', 'year': 1997, 'rating': 8.9,
         'description': 'История любви на тонущем корабле. Джек и Роуз встречаются на борту "Титаника".'},
    ],
    'интерстеллар': [
        {'id': 11, 'title': 'Интерстеллар', 'year': 2014, 'rating': 9.0,
         'description': 'Путешествие сквозь червоточину в поисках нового дома для человечества.'},
    ],
    'бойцовский клуб': [
        {'id': 12, 'title': 'Бойцовский клуб', 'year': 1999, 'rating': 8.8,
         'description': 'Офисный работник и таинственный Тайлер Дёрден создают подпольный клуб.'},
    ],
    'зеленая миля': [
        {'id': 13, 'title': 'Зеленая миля', 'year': 1999, 'rating': 9.0,
         'description': 'История надзирателя блока смертников и необычного заключённого.'},
    ],
    'побег из шоушенка': [
        {'id': 14, 'title': 'Побег из Шоушенка', 'year': 1994, 'rating': 9.3,
         'description': 'Банкира Энди Дюфрейна отправляют в тюрьму за убийство, которого он не совершал.'},
    ],
}

# Временное хранилище для результатов поиска
user_search_results = {}


def search_local_movies(query: str):
    """Поиск фильмов в локальной базе данных"""
    query_lower = query.lower().strip()

    # Прямое совпадение с ключом
    if query_lower in LOCAL_MOVIES:
        return LOCAL_MOVIES[query_lower]

    # Частичное совпадение
    results = []
    for key, movies in LOCAL_MOVIES.items():
        if key in query_lower or query_lower in key:
            results.extend(movies)

    return results


@bot.message_handler(commands=['search'])
def search_movie_command(message: Message):
    """Обработчик команды /search <название фильма>"""
    try:
        user = get_or_create_user(message)
        if not user.is_premium and user.daily_searches >= 5:
            bot.reply_to(message, "Лимит 5 запросов/день. /subscribe для безлимита")
            return

        # Получаем текст после команды
        query_parts = message.text.split(maxsplit=1)

        if len(query_parts) < 2:
            bot.reply_to(
                message,
                "❓ *Как использовать:*\n"
                "`/search <название фильма>`\n\n"
                "📝 *Примеры:*\n"
                "`/search Матрица`\n"
                "`/search Форсаж`\n"
                "`/search Титаник`",
                parse_mode='Markdown'
            )
            return

        query = query_parts[1]

        # Отправляем уведомление о начале поиска
        bot.reply_to(message, f"🔍 Ищу фильмы по запросу: *{query}*...", parse_mode='Markdown')

        # Ищем фильмы в локальной базе
        movies = search_kinopoisk_api(query)  # уже написан в kinopoisk_api.py!

        if not movies:
            # Показываем доступные категории
            available = "\n".join([f"• {key.title()}" for key in LOCAL_MOVIES.keys()])
            error_msg = (
                f"😔 По запросу *{query}* ничего не найдено.\n\n"
                f"📋 *Доступные фильмы:*\n{available}\n\n"
                f"💡 *Совет:* Попробуйте одно из названий выше."
            )
            bot.reply_to(message, error_msg, parse_mode='Markdown')
            save_search_history(message, query)
            return

        # Сохраняем результаты для пользователя
        user_search_results[user.user_id] = movies

        # Создаем клавиатуру с кнопками-результатами
        markup = types.InlineKeyboardMarkup(row_width=1)
        for i, movie in enumerate(movies[:10]):
            title = movie.get('title', 'Без названия')
            year = f" ({movie.get('year')})" if movie.get('year') else ""
            rating = f" ⭐ {movie.get('rating')}" if movie.get('rating') else ""
            btn_text = f"🎬 {title}{year}{rating}"
            callback_data = f"movie_{user.user_id}_{i}"
            markup.add(types.InlineKeyboardButton(btn_text, callback_data=callback_data))

        bot.reply_to(
            message,
            f"✅ Найдено *{len(movies)}* фильмов по запросу *{query}*:\n\nВыберите фильм для просмотра деталей:",
            reply_markup=markup,
            parse_mode='Markdown'
        )

        # Сохраняем поиск в историю
        save_search_history(message, query)

    except Exception as e:
        error_msg = (
            "😔 *Произошла ошибка при поиске.*\n\n"
            f"Ошибка: {str(e)}\n\n"
            "Пожалуйста, попробуйте позже."
        )
        bot.reply_to(message, error_msg, parse_mode='Markdown')
        print(f"Ошибка в search_movie_command: {e}")


@bot.callback_query_handler(func=lambda call: call.data.startswith('movie_'))
def handle_movie_selection(call):
    """Обработчик выбора фильма из результатов поиска"""
    try:
        user_id = int(call.data.split('_')[1])
        movie_index = int(call.data.split('_')[2])

        # Проверяем, что пользователь тот же
        if call.from_user.id != user_id:
            bot.answer_callback_query(call, "❌ Это не ваш результат поиска!", show_alert=True)
            return

        movies = user_search_results.get(user_id, [])
        if movie_index >= len(movies):
            bot.answer_callback_query(call, "❌ Фильм не найден", show_alert=True)
            return

        movie = movies[movie_index]

        # Формируем сообщение с деталями фильма
        title = movie.get('title', 'Без названия')
        year = movie.get('year')
        rating = movie.get('rating')
        description = movie.get('description')

        movie_details = f"🎬 *{title}*"
        if year:
            movie_details += f"\n📅 *Год:* {year}"
        if rating:
            movie_details += f"\n⭐ *Рейтинг:* {rating}"
        if description:
            movie_details += f"\n\n📖 *Описание:*\n{description[:500]}..."

        # Сохраняем выбранный фильм в историю
        save_search_history(call.message, call.message.text.replace("/search ", ""), movie)

        # Отправляем детали
        bot.edit_message_text(
            movie_details,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode='Markdown'
        )

        bot.answer_callback_query(call, "✅ Информация о фильме загружена!")

    except Exception as e:
        bot.answer_callback_query(call, f"❌ Ошибка: {str(e)}", show_alert=True)
        print(f"Ошибка в handle_movie_selection: {e}")


@bot.message_handler(commands=['history'])
def history_command(message: Message):
    """Обработчик команды /history - показывает историю поиска"""
    try:
        user = get_or_create_user(message)
        history_text = get_user_history_formatted(message)
        bot.reply_to(message, history_text, parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, f"😔 Ошибка при получении истории: {str(e)}")
        print(f"Ошибка в history_command: {e}")
