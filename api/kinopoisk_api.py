import requests
from config import API_KEY


class KinopoiskAPI:
    """Класс для работы с API Кинопоиска"""

    BASE_URL = "https://api.kinopoisk.dev/v1.4"

    def __init__(self):
        self.headers = {
            "X-API-KEY": API_KEY,
            "Content-Type": "application/json"
        }

    def search_movie(self, query: str, limit: int = 5):
        """
        Поиск фильмов по названию.
        Возвращает список фильмов.
        """
        url = f"{self.BASE_URL}/movie/search"
        params = {
            "query": query,
            "limit": limit
        }

        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()

            movies = []
            for doc in data.get('docs', []):
                movies.append({
                    'id': doc.get('id'),
                    'title': doc.get('name') or doc.get('alternativeName'),
                    'year': doc.get('year'),
                    'rating': doc.get('rating', {}).get('kp'),
                    'description': doc.get('description'),
                    'poster': doc.get('poster', {}).get('url')
                })

            return movies

        except requests.exceptions.RequestException as e:
            print(f"Ошибка API: {e}")
            return []

    def get_movie_details(self, movie_id: int):
        """Получение детальной информации о фильме по ID"""
        url = f"{self.BASE_URL}/movie/{movie_id}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка получения деталей: {e}")
            return None
