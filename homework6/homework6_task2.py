# Завдання 2: Робота з зовнішніми пакетами
import requests

url = "https://vintest.org.ua/"

try:
    # Завантажує сторінку
    response = requests.get(url)
    # Перевірка, чи не виникло помилок
    response.raise_for_status()

    file_path = "vintest.org.ua.txt"
    # Збереження у текстовий файл
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"Cторінка збережена у файл: {file_path}")
except requests.exceptions.HTTPError as e:
    print(e)
