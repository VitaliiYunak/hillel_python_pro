# Завдання 7: Декоратор для логування викликів методів

def log_methods(cls):
    # Отримуємо всі атрибути класу
    for attr_name, attr_value in cls.__dict__.items():
        # Перевіряємо, чи є атрибут методом і чи не є він магічним
        if callable(attr_value) and not attr_name.startswith("__"):
            original_method = attr_value

            def logged_method(self, *args, **kwargs):
                # Логування виклику методу
                print(f"Logging: {attr_name} called with {args}")
                return original_method(self, *args, **kwargs)

            setattr(cls, attr_name, logged_method)
    return cls


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


if __name__ == "__main__":
    obj = MyClass()
    obj.add(5, 3)  # Logging: add called with (5, 3)
    obj.subtract(5, 3)  # Logging: subtract called with (5, 3)
