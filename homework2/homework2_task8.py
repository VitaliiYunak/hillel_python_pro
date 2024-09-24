# Завдання 8: Зберігання налаштувань користувача

def create_user_settings(theme, language, notifications):
    settings = {
        "theme": theme,
        'language': language,
        "notifications": notifications
    }

    def set_value(key, value):
        if key in settings:
            settings[key] = value
        else:
            print(f"Відсутнє налаштування: {key}")

    def show_value():
        return settings

    return set_value, show_value


set_setting, show_setting = create_user_settings("dark", "ua", "default")

print("Hалаштування:", show_setting())

set_setting('theme', 'light')
set_setting('language', 'en')

print("Змінені налаштування:", show_setting())
