# 10. Архівування та зберігання великих даних

import zipfile
import os


class ZipArchiveManager:
    """
    Менеджер контексту для архівування файлів.
    """

    def __init__(self, archive_name):
        self.archive_name = archive_name
        self.zip_file = None

    def __enter__(self):
        # Створення ZIP архіву
        self.zip_file = zipfile.ZipFile(self.archive_name, 'w')
        return self.zip_file

    def add_file(self, file_name):
        """
        Додає файл до архіву.
        """
        if os.path.isfile(file_name):
            self.zip_file.write(file_name, os.path.basename(file_name))
        else:
            print(f"{file_name} не знайдено:")

    def __exit__(self, except_type, except_value, traceback):
        # Закриття архіву
        if self.zip_file:
            self.zip_file.close()


if __name__ == "__main__":
    name_zip_archiv = "archive.zip"
    with ZipArchiveManager(name_zip_archiv) as zip_manager:
        # Додаємо файли до архіву
        zip_manager.write("log.txt")
        zip_manager.write("log_new.txt")
        print(f"Створено архів: {name_zip_archiv}")
