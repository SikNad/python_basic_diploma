from database.models import User


def get_or_create_user(message):
    """
    Получает существующего пользователя или создает нового.
    Вызывать в начале каждого обработчика.

    Args:
        message: сообщение от пользователя (telebot.types.Message)

    Returns:
        User: объект пользователя из базы данных
    """
    user_id = message.from_user.id

    user, created = User.get_or_create(
        user_id=user_id,
        defaults={
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        }
    )

    if created:
        print(f"👤 Создан новый пользователь: {user.first_name} (ID: {user_id})")

    return user
