from database.models import SearchHistory, User
from database.user_service import get_or_create_user
import datetime


def save_search_history(message, query, movie_result=None):
    """
    Сохраняет историю поиска в базу данных.
    """
    try:
        user = get_or_create_user(message)

        SearchHistory.create(
            user=user,
            query=query,
            movie_title=movie_result.get('title') if movie_result else None,
            movie_year=movie_result.get('year') if movie_result else None,
            rating=str(movie_result.get('rating')) if movie_result and movie_result.get('rating') else None,
            searched_at=datetime.datetime.now()
        )
        print(f"💾 Сохранен поиск: '{query}' для пользователя {user.user_id}")
    except Exception as e:
        print(f"❌ Ошибка сохранения истории: {e}")


def get_user_history(message, limit=10):
    """Получает последние поиски пользователя"""
    try:
        user = get_or_create_user(message)

        history = (SearchHistory
                   .select()
                   .where(SearchHistory.user == user)
                   .order_by(SearchHistory.searched_at.desc())
                   .limit(limit))

        return list(history)
    except Exception as e:
        print(f"❌ Ошибка получения истории: {e}")
        return []


def get_user_history_formatted(message, limit=10):
    """Возвращает историю в отформатированном виде для отправки пользователю"""
    history = get_user_history(message, limit)

    if not history:
        return "📭 У вас пока нет истории поиска. Попробуйте найти что-нибудь: /search Матрица"

    result = "📜 *Ваша история поиска:*\n\n"
    for i, item in enumerate(history, 1):
        result += f"{i}. 🎬 *Запрос:* {item.query}\n"
        if item.movie_title:
            result += f"   📽 Результат: {item.movie_title}"
            if item.movie_year:
                result += f" ({item.movie_year})"
            if item.rating:
                result += f" | ⭐ Рейтинг: {item.rating}"
            result += "\n"
        result += f"   🕐 {item.searched_at.strftime('%d.%m.%Y %H:%M')}\n\n"

    return result
