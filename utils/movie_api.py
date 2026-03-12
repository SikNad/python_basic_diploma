import requests
from config import API_KEY


class KinopoiskAPI:
    def __init__(self):
        self.base_url = "https://kinopoiskapiunofficial.tech"
        self.headers = {
            'X-API-KEY': API_KEY,
            'Content-Type': 'application/json'
        }

    def search_by_keyword(self, keyword, page=1):
        """Поиск фильмов по ключевому слову"""
        url = f"{self.base_url}/api/v2.1/films/search-by-keyword"
        params = {
            'keyword': keyword,
            'page': page
        }

        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Ошибка API при поиске: {e}")
            return None

    def format_movie_info(self, film):
        """Форматирование информации о фильме"""
        name = film.get('nameRu') or film.get('nameEn') or 'Неизвестно'
        year = film.get('year', 'Неизвестно')
        rating = film.get('rating', 'Н/Д')

        text = f"🎬 *{name}*\n"
        text += f"📅 Год: {year}\n"
        text += f"⭐ Рейтинг: {rating}\n"

        if film.get('countries'):
            countries = [c.get('country', '') for c in film['countries']]
            text += f"🌍 Страны: {', '.join(countries[:3])}\n"

        if film.get('genres'):
            genres = [g.get('genre', '') for g in film['genres']]
            text += f"🎭 Жанры: {', '.join(genres[:3])}\n"

        return text
