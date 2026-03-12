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

    def get_films_by_rating(self, rating_from=7, rating_to=10, year_from=2010, year_to=2025):
        """Поиск фильмов по рейтингу"""
        # Для реального API Кинопоиска нужен другой эндпоинт
        # Это упрощенная версия, позже уточним точный метод
        url = f"{self.base_url}/api/v2.2/films"
        params = {
            'ratingFrom': rating_from,
            'ratingTo': rating_to,
            'yearFrom': year_from,
            'yearTo': year_to,
            'order': 'RATING',
            'type': 'FILM'
        }

        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Ошибка API при поиске по рейтингу: {e}")
            return None

    def get_films_by_budget(self, budget_from=0, budget_to=1000000):
        """Поиск фильмов по бюджету (в долларах)"""
        # Аналогично, уточним эндпоинт позже
        pass

    def get_movie_details(self, film_id):
        """Получение детальной информации о фильме"""
        url = f"{self.base_url}/api/v2.2/films/{film_id}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Ошибка API при получении деталей: {e}")
            return None
