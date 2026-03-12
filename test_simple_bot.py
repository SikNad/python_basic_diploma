import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Привет! Я простой тестовый бот")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Эхо: {message.text}")

print("🤖 Запуск простого тестового бота...")
bot.infinity_polling()
