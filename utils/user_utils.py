from models import User


def get_or_create_user(user_id, username=None):
    """
    Получить пользователя из БД или создать нового
    """
    try:
        user, created = User.get_or_create(
            user_id=user_id,
            defaults={'username': username}
        )
        if created:
            print(f"✅ Создан новый пользователь: {user_id} (@{username})")
        else:
            print(f"👤 Найден существующий пользователь: {user_id}")
        return user
    except Exception as e:
        print(f"❌ Ошибка при работе с БД: {e}")
        # Создаём заглушку, если БД недоступна
        return type('User', (), {'id': user_id})()
