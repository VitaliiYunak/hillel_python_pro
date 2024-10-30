# Завдання 1. Перевірка валідності email

import re


def checking_email(email):
    """
    Перевірка email
    """
    pattern_email = r'\b[a-zA-Z0-9](?:[a-zA-Z0-9.]*[a-zA-Z0-9])?@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,6}'

    return bool(re.match(pattern_email, email))


if __name__ == "__main__":
    print(checking_email("vitalii.yunak@gmail.com"))
    print(checking_email(".yunak@gmail.com"))
    print(checking_email("vitalii.yunak.@gmail.com"))
    print(checking_email("yunak@.com"))
    print(checking_email("yunak@gmail"))
    print(checking_email("юнак@gmail.com"))
