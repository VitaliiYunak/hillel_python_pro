# Завдання 8. Перевірка на наявність шаблону в тексті

import re


def presence_template(text):
    pattern = r'\b[A-Z]{2}\d{2}[A-Z]{2}\d{2}$'
    return bool(re.search(pattern, text))


if __name__ == "__main__":
    text = "Ваш код: AB12CD34"
    result = presence_template(text)
    print(result)
