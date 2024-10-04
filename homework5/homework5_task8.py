# 8. Конфігурація через контекстні менеджери

import json


class ConfigJson:
    """
    Контекстний менеджер для роботи з файлами конфігурацій у форматі JSON.
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.config = {}

    def __enter__(self):
        # Читання конфігурації з файлу
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                self.config = json.load(file)
        # Якщо файл не знайдено, ініціалізуємо порожню конфігурацію
        except FileNotFoundError:
            self.config = {}
        return self.config

    def __exit__(self, except_type, except_value, traceback):
        # Запис зміни конфігурації у файл
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.config, file, indent=4)


if __name__ == "__main__":
    with ConfigJson('setting.json') as config:
        config['ENGINE'] = 'django.db.backends.sqlite3'
        config['NAME'] = 'db.sqlite3'
