# 3. Збір статистики про зображення

import os
import csv
from PIL import Image
from pathlib import Path


class ImagesData:
    """
    Відкриває зображення, витягує з нього формат, розмір, ширину, висоту
    """
    def __init__(self, directory):
        self.directory = directory
        image_format = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        self.images = []
        self.current_index = 0

        # Перевіряє, чи є файл у теці графічним зображенням. Якщо так, зберігає у список
        for filename in os.listdir(self.directory):
            is_image = Path(filename)
            if is_image.suffix.lower() in image_format:
                self.images.append(str(is_image))
        print(f"Зображення в теці '{directory}':")
        print(self.images)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.images):
            image_path = os.path.join(self.directory, self.images[self.current_index])
            self.current_index += 1

            with Image.open(image_path) as img:
                data = {
                    "ім'я файлу": self.images[self.current_index - 1],
                    'формат': img.format,
                    'розмір': img.size,
                    'ширина': img.width,
                    'висота': img.height
                }
                return data
        else:
            raise StopIteration


def save_to_csv(directory, csv_file):
    """
    Метадані зображень зберігаються до csv-файлу
    :param directory: тека, в якій знаходяться зображення
    :param csv_file: імя вихідного csv-файлу
    """
    image_info = ImagesData(directory)

    with open(csv_file, mode='w', newline='') as file:

        # Метадані формуються у вигляді словника
        writer = csv.DictWriter(file,
                                delimiter=";",
                                fieldnames=["ім'я файлу", "формат", "розмір", "ширина", "висота"])
        writer.writeheader()

        for data in image_info:
            writer.writerow(data)
    print(f"Метадані зображень збережені у файлі: {csv_file}")


if __name__ == "__main__":
    save_to_csv("images", "images.csv")
