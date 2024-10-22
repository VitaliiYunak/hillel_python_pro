# Задача 2: паралельна обробка зображень

import os
from concurrent.futures import ProcessPoolExecutor
from PIL import Image

images_to_process = [
    "them-snapshots-EZ.jpg",
    "dery-triyatna.jpg",
    "them-snapshots.jpg",
    "elisabeth-arnold.jpg",
    "sherry-christian.jpg"
]


def resize_image(image_path, output_size=(960, 720)):
    """
    Змінює розмір зображення до заданих розмірів.
    :param image_path: Шлях до зображення.
    :param output_size: Новий розмір.
    :return: Шлях до збереженого зображення.
    """
    try:
        with Image.open(image_path) as img:
            img = img.resize(output_size)
            output_path = f"new_{os.path.basename(image_path)}"
            img.save(output_path)
            return output_path
    except Exception as e:
        print(f"Помилка зміни розміру файла {image_path}: {e}")
        return None


def image_processing(image_path):
    """
    Обробляє кілька зображень одночасно.
    """
    with ProcessPoolExecutor() as executor:
        processing = list(executor.map(resize_image, image_path))

    for process in processing:
        if process:
            print(f"Змінено розмір та збережено новий файл: {process}")


if __name__ == "__main__":
    image_processing(images_to_process)
