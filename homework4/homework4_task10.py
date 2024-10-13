# Завдання 10: Метаклас для контролю створення класів

class SingletonMeta(type):
    """
    Гарантує, що клас може мати лише один екземпляр
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Якщо екземпляр класу вже створений, повертаємо його
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            return instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1 is obj2)  # True
