# Завдання 8: Перевірка успадкування та методів класу

def analyze_inheritance(cls):
    # Отримуємо базовий клас
    bases = cls.__bases__
    print(bases)
    inheritance = set()

    # Отримуємо методи базового класу
    for base in bases:
        for name, method in base.__dict__.items():
            if callable(method) and not name.startswith("__"):
                inheritance.add((name, base.__name__))

    print(f"Клас {cls.__name__} наслідує:")
    for method_name, base_name in inheritance:
        print(f"- {method_name} з {base_name}")


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


if __name__ == "__main__":
    analyze_inheritance(Child)
