# Завдання 2: Динамічний виклик функцій

def call_function(obj, method_name, *args):
    """
    Перевіряє, чи має об'єкт метод з назвою, що передається. Якщо все правильно,
    викликає метод з аргументами *args.
    """
    if hasattr(obj, method_name):
        result = getattr(obj, method_name)
        return result(*args)


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


if __name__ == "__main__":
    calc = Calculator()
    print(call_function(calc, "add", 10, 5))  # 15
    print(call_function(calc, "subtract", 10, 5))  # 5
