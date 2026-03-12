import telebot

# Вставьте ваш токен прямо сюда для теста
TOKEN = "8601470478:AAEsIAJo-a9YX3mbazWo5E7ZOL6YzjHprJE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ Бот работает!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, f"Вы написали: {message.text}")

print("🚀 Запуск простейшего бота...")
print(f"Используем токен: {TOKEN[:10]}...")
bot.infinity_polling()
