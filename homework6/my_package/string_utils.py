# Завдання 1: Створення власного пакету

def to_upper(text):
    """
    Перетворює текст в верхній регістр.
    """
    return text.upper()


def strip_spaces(text):
    """
    Видаляє пробіли на початку та в кінці рядка.
    """
    return text.strip()


if __name__ == "__main__":
    print(to_upper("Hello, world!"))
    print(strip_spaces(" Hello, world!  "))
