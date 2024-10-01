# Завдання 1: Перевірка типів і атрибутів об'єктів

def analyze_object(value):
    """
    info: список атрибутів і методів об'єкта
    result: імя та тип кожного елемента списку
    """
    print(type(value))
    info = dir(value)
    for item in info:
        result = type(getattr(obj, item))
        print(f"{item}: {result}")


class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


if __name__ == "__main__":
    obj = MyClass("World")
    analyze_object(obj)
