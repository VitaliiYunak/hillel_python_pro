# Задача 1: завантаження файлів із мережі

import threading
import time
import requests
import os

# Список файлів для завантаження
urls = [
        'https://testportal.gov.ua//wp-content/uploads/2024/01/nakaz-vid-24.01.2024-5.pdf',
        'https://testportal.gov.ua//wp-content/uploads/2024/01/nakaz-vid-24.01.2024-4.pdf',
        'https://testportal.gov.ua//wp-content/uploads/2024/02/Kalendarnyj-plan__vstupni-do-magistratury_2024_scan.pdf',
        'https://testportal.gov.ua//wp-content/uploads/2024/01/NT_2024-Programa-ist_Ukr.pdf'
    ]


def download_file(download_url):
    """
    # Завантаження файлу
    :param download_url: шлях до файлу
    """
    try:
        # Отримання імені файлу з URL
        file_name = os.path.basename(download_url)
        # Завантаження файлу
        response = requests.get(download_url)
        response.raise_for_status()
        # Запис файлу
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"'{file_name}' завантажено")
    except Exception as e:
        print(f'Помилка при завантаженні {url}: {e}')


if __name__ == "__main__":

    threads = []
    start = time.time()
    # Створення та запуск потоків
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()
    # Завершення всіх потоків
    for thread in threads:
        thread.join()

    print(f"Файли завантажені. Час виконання: {time.time() - start:0.2f}")
