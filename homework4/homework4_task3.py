import importlib
import inspect


def analyze_module(module_name):
    try:
        # Імпортується модуль
        module = importlib.import_module(module_name)
        print(f"Модуль: {module_name}")
    except ModuleNotFoundError:
        print(f"Модуль '{module_name}' не знайдено.")
        return

    # Список класів і функцій
    classes = inspect.getmembers(module, inspect.isclass)
    functions = inspect.getmembers(module, inspect.isfunction)

    # Функції
    if functions:
        print("Функції:")
        for func_name, func_obj in functions:
            print(f" - {func_name}: {inspect.signature(func_obj)}")
    else:
        print(f" - Немає функцій у класі {module}")

    # Класи
    if classes:
        print("Класи:")
        for class_name, class_obj in classes:
            print(f" - {class_name}: {inspect.signature(class_obj)}")
    else:
        print(f"- Немає класів у модулі: {module}")


if __name__ == '__main__':
    analyze_module("math")
