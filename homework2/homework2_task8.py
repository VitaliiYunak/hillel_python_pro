# Завдання 8: Зберігання налаштувань користувача

def create_user_settings():
    settings = {
        "theme": "dark",
        'language': "ua",
        "notifications": "default"
    }

    def set_value(key, value):
        if key in settings:
            settings[key] = value
        else:
            print(f"Відсутнє налаштування: {key}")

    def show_value():
        return settings

    return set_value, show_value


set_setting, show_setting = create_user_settings()

print("Hалаштування:", show_setting())

set_setting('theme', 'light')
set_setting('language', 'en')

print("Змінені налаштування:", show_setting())
