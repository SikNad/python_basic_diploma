import requests

API_KEY = "0c2f2d69-e44c-4b8f-90d1-63aeb2161d52"
url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/301"
headers = {
    'X-API-KEY': API_KEY,
    'Content-Type': 'application/json'
}

print("🔍 Проверяем API ключ...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ КЛЮЧ РАБОТАЕТ!")
    data = response.json()
    print(f"🎬 Название: {data.get('nameRu')}")
    print(f"📅 Год: {data.get('year')}")
    print(f"⭐️ Рейтинг: {data.get('ratingKinopoisk')}")
else:
    print(f"❌ Ошибка {response.status_code}: {response.text}")
