from loader import bot
from telebot.types import Message
from keyboards.reply import get_main_keyboard


@bot.message_handler(commands=['help'])
def help_command(message: Message):
    """Помощь по командам"""
    bot.reply_to(
        message,
        "🤖 *Помощь по командам бота:*\n\n"
        "🔍 */search <название>* — поиск фильма\n"
        "   Пример: `/search Матрица`\n\n"
        "📜 */history* — показать историю поиска\n\n"
        "🆘 */help* — показать это сообщение\n\n"
        "✨ *Совет:* Можно использовать клавиатуру под полем ввода!",
        parse_mode='Markdown',
        reply_markup=get_main_keyboard()
    )
