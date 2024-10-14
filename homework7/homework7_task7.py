"""
Завдання 7. Тестування з використанням фікстур та тимчасових файлів
"""
import os
import pytest


class FileProcessor:
    """
    Записує дані у файл та читає дані з файлу.
    """
    @staticmethod
    def write_to_file(file_path: str, data: str):
        """Записує дані у файл."""
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """Читає дані з файлу."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файлу {file_path} не існує.")
        with open(file_path, 'r', encoding="utf-8") as file:
            return file.read()


def test_file_write_read(tmpdir):
    """Запис у файл та читання з файлу.
    """
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


def test_file_write_empty_string(tmpdir):
    """Запис порожнього рядка.
    """
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)
    assert content == ""


def test_file_write_large_data(tmpdir):
    """Запис великих обсягів даних.
    """
    file = tmpdir.join("testfile.txt")
    data = "Hello, world!" * 1000
    FileProcessor.write_to_file(file, data)
    content = FileProcessor.read_from_file(file)
    assert content == data


def test_read_nonexistent_file(tmpdir):
    """Наявність винятків, якщо файл не знайдено.
    """
    notexist_file = tmpdir.join("testfile.txt")
    with pytest.raises(FileNotFoundError, match=f"Файл {notexist_file} не знайдено."):
        FileProcessor.read_from_file(notexist_file)
