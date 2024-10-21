import redis
import time
import uuid

# Підключення до Redis
con = redis.Redis(host='localhost', port=6379, db=0)


def create_session(user_id):
    """
    Нова сесія користувача
    """
    session_token = str(uuid.uuid4())
    login_time = int(time.time())
    session_data = {
        'user_id': user_id,
        'session_token': session_token,
        'login_time': login_time
    }
    # Зберігаємо сесію в Redis
    con.hset(f'session:{session_token}', mapping=session_data)
    # Налаштуємо TTL (30 хвилин)
    con.expire(session_token, 1800)
    return session_token


def get_session(session_token):
    """
    Активна сесія користувача.
    """
    session_data = con.hgetall(f'session:{session_token}')
    if session_data:
        decoded_session_data = {}
        for k, v in session_data.items():
            decoded_session_data[k.decode('utf-8')] = v.decode('utf-8')
        return decoded_session_data
    return None


def update_session(session_token):
    """
    Оновлення часу останньої активності користувача
    """
    current_time = int(time.time())
    con.hset(f'session:{session_token}', 'login_time', str(current_time))
    con.expire(f'session:{session_token}', 1800)


def delete_session(session_token):
    """
    Видалення сесії після виходу користувача з системи
    """
    con.delete(f'session:{session_token}')
