# Завдання 6. Перевірка валідності пароля

import re


def password_verification(password: str) -> bool:
    """
    Перевірка валідності пароля
    """
    if len(password) < 8:
        return False

    # Наявність цифри
    if not re.search(r'\d', password):
        return False

    # Наявність великої літери
    if not re.search(r'[A-Z]', password):
        return False

    # Наявність малої літери
    if not re.search(r'[a-z]', password):
        return False

    # Наявність спеціального символу
    if not re.search(r'[!@#$%&*.?]', password):
        return False

    return True


if __name__ == "__main__":
    password = "Pa$$w0rD"
    if password_verification(password):
        print("Пароль надійний")
    else:
        print("Пароль ненадійний")
