# Завдання 4. Форматування дати

import re


def convert_date(date):
    """
    Зміна формату дати
    """
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    # Змінюємо формат на YYYY-MM-DD
    formated_date = re.sub(pattern, r'\3-\2-\1', date)
    return formated_date


if __name__ == "__main__":
    date_now = '30/10/2024'
    print(date_now)
    new_date = convert_date(date_now)
    print(f"Форматована дата: {new_date}")
