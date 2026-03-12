from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def get_main_keyboard():
    """Главная клавиатура с командами поиска"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton("🎬 Поиск по названию"),
        KeyboardButton("⭐ Поиск по рейтингу"),
        KeyboardButton("💰 Низкий бюджет"),
        KeyboardButton("💎 Высокий бюджет"),
        KeyboardButton("📋 История поиска"),
        KeyboardButton("❓ Помощь")
    )
    return keyboard


def get_cancel_keyboard():
    """Клавиатура с кнопкой отмены"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("❌ Отмена"))
    return keyboard


def get_pagination_keyboard(page, total_pages, prefix):
    """Инлайн-клавиатура для пагинации"""
    keyboard = InlineKeyboardMarkup(row_width=3)

    buttons = []
    if page > 1:
        buttons.append(InlineKeyboardButton("⬅️", callback_data=f"{prefix}_prev_{page - 1}"))

    buttons.append(InlineKeyboardButton(f"{page}/{total_pages}", callback_data="noop"))

    if page < total_pages:
        buttons.append(InlineKeyboardButton("➡️", callback_data=f"{prefix}_next_{page + 1}"))

    keyboard.add(*buttons)
    return keyboard
