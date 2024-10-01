# Завдання 5: Модифікація атрибутів під час виконання

class MutableClass:

    def __init__(self):
        self.name = None

    def add_attribute(self, name, value):
        """Додає атрибут з заданим ім'ям та значенням."""
        setattr(self, name, value)
        print(f"Додано атрибут '{name}' із значенням '{value}'")

    def remove_attribute(self, name):
        """Видаляє атрибут з заданим ім'ям, якщо він існує."""
        if hasattr(self, name):
            delattr(self, name)
            print(f"Атрибут '{name}' видалений")
        else:
            print(f"Виникла помилка, атрибут '{name}' видалений.")


if __name__ == "__main__":
    obj = MutableClass()
    obj.add_attribute("name", "Python")
    obj.remove_attribute("name")
    obj.remove_attribute("name")
