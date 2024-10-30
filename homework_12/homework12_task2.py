# Завдання 2. Пошук телефонних номерів

import re


def find_phone(text):
    """Пощук телефонних номерів
    """
    pattern_phone = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    phone_numbers = re.findall(pattern_phone, text)

    return phone_numbers


if __name__ == "__main__":
    text = """
    (123) 456-7890
    123-456-7890
    123.456.7890
    1234567890
    (123)45-67-890
    """

    phone_numbers = find_phone(text)
    print(phone_numbers)
