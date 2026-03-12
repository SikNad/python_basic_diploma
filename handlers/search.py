from loader import bot
from telebot.types import Message
from utils.movie_api import KinopoiskAPI
from keyboards.reply import get_main_keyboard
import logging

print("✅ Модуль search.py ЗАГРУЖЕН")  # 👈 ЭТУ СТРОКУ ДОБАВЬТЕ ЗДЕСЬ!

api = KinopoiskAPI()


@bot.message_handler(commands=['search'])
def search_movie(message: Message):
    """Поиск фильма по названию"""
    # 👇 ДОБАВЬТЕ ЭТИ СТРОКИ
    print(f"🔔 ПОЛУЧЕНА КОМАНДА /search!")
    print(f"   От пользователя: {message.from_user.id}")
    print(f"   Текст: {message.text}")
    print(f"   Чат ID: {message.chat.id}")

    try:
        # Получаем название фильма из сообщения
        parts = message.text.split(maxsplit=1)

        if len(parts) < 2:
            print("❌ Нет названия фильма")
            bot.reply_to(
                message,
                "❌ Пожалуйста, укажите название фильма.\n"
                "Пример: /search Матрица"
            )
            return

        query = parts[1]
        print(f"📝 Ищем фильм: {query}")

        # Отправляем сообщение о начале поиска
        waiting_msg = bot.send_message(
            message.chat.id,
            f"🔍 Ищу фильмы по запросу: '{query}'..."
        )
        print("✅ Сообщение ожидания отправлено")

        # Выполняем поиск через API
        print("🔄 Отправляю запрос к API...")
        results = api.search_by_keyword(query)
        print(f"📊 Результат API: {results is not None}")

        # Удаляем сообщение ожидания
        bot.delete_message(message.chat.id, waiting_msg.message_id)
        print("✅ Сообщение ожидания удалено")

        if not results or not results.get('films'):
            print("❌ Фильмы не найдены")
            bot.reply_to(
                message,
                f"😕 По запросу '{query}' ничего не найдено.\n"
                "Попробуйте другое название."
            )
            return

        # Показываем первые 5 результатов
        films = results.get('films', [])[:5]
        print(f"🎬 Найдено фильмов: {len(films)}")

        for i, film in enumerate(films, 1):
            print(f"   Фильм {i}: {film.get('nameRu', 'Без названия')}")
            film_info = api.format_movie_info(film)

            # Отправляем фото, если есть
            if film.get('posterUrl'):
                try:
                    bot.send_photo(
                        message.chat.id,
                        film['posterUrl'],
                        caption=film_info,
                        parse_mode='Markdown'
                    )
                    print(f"✅ Постер отправлен для фильма {film.get('nameRu')}")
                    print("📤 Сообщение отправлено в Telegram")
                except Exception as e:
                    print(f"   ⚠️ Ошибка отправки постера: {e}")
                    bot.send_message(
                        message.chat.id,
                        film_info,
                        parse_mode='Markdown'
                    )
            else:
                bot.send_message(
                    message.chat.id,
                    film_info,
                    parse_mode='Markdown'
                )
                print(f"   ✅ Текст отправлен")

        bot.send_message(
            message.chat.id,
            "✅ Поиск завершен. Используйте /help для других команд.",
            reply_markup=get_main_keyboard()
        )
        print("🏁 Поиск завершен")

    except Exception as e:
        print(f"💥 ОШИБКА: {str(e)}")
        bot.reply_to(
            message,
            f"❌ Произошла ошибка при поиске: {str(e)}"
        )
