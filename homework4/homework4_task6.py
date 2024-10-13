# Завдання 6: Інтерсепція методів класу (Proxy)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        # Отримує метод з об'єкта
        original_attr = getattr(self._obj, name)

        def wrapped(*args, **kwargs):
            # Логування виклику методу
            print(f"Calling method: {name} with args: {args}")
            return original_attr(*args, **kwargs)
        return wrapped


class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"


if __name__ == "__main__":
    obj = MyClass()
    proxy = Proxy(obj)

    print(proxy.greet("Alice"))
