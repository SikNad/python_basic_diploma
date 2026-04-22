#!/usr/bin/env python3
"""
Тест подключения к Telegram API
Запустите: python test_connection.py
"""

import requests
import time

TOKEN = "8601470478:AAEsIAJo-a9YX3mbazWo5E7ZOL6YzjHprJE"

print("=" * 60)
print("🔍 ДИАГНОСТИКА ПОДКЛЮЧЕНИЯ К TELEGRAM")
print("=" * 60)

# 1. Проверка интернета
print("\n1. Проверка интернет-соединения...")
try:
    response = requests.get("https://www.google.com", timeout=5)
    print("   ✅ Интернет работает")
except Exception as e:
    print(f"   ❌ Нет интернета: {e}")
    exit(1)

# 2. Проверка доступа к Telegram API
print("\n2. Проверка доступа к api.telegram.org...")
try:
    response = requests.get("https://api.telegram.org", timeout=5)
    print(f"   ✅ api.telegram.org доступен (статус: {response.status_code})")
except Exception as e:
    print(f"   ❌ api.telegram.org НЕДОСТУПЕН!")
    print(f"   Ошибка: {e}")
    print("   💡 Решение: включите VPN или проверьте настройки сети")

# 3. Проверка токена бота
print("\n3. Проверка токена бота...")
try:
    url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    response = requests.get(url, timeout=10)
    data = response.json()

    if data.get('ok'):
        bot_info = data.get('result', {})
        print("   ✅ Токен правильный!")
        print(f"   👤 Бот: @{bot_info.get('username')}")
        print(f"   📛 Имя: {bot_info.get('first_name')}")
        print(f"   🆔 ID: {bot_info.get('id')}")
    else:
        print(f"   ❌ Токен НЕПРАВИЛЬНЫЙ!")
        print(f"   Ответ: {data}")
except Exception as e:
    print(f"   ❌ Ошибка при проверке токена: {e}")

print("\n" + "=" * 60)
print("🏁 ДИАГНОСТИКА ЗАВЕРШЕНА")
print("=" * 60)
