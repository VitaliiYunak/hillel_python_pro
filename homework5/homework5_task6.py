# 6. Ітерація через файли в каталозі

import os


class FileIterator:
    """Ітератор для обходу файлів у каталозі."""
    def __init__(self, directory):
        self.directory = directory
        self.files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        :return: name, size - імя та розмір файлу
        """
        if self.current_index < len(self.files):
            name = self.files[self.current_index]
            file_path = os.path.join(self.directory, name)
            size = os.path.getsize(file_path)
            self.current_index += 1
            return name, size
        else:
            raise StopIteration


if __name__ == "__main__":
    directory_path = "./files"
    file_iterator = FileIterator(directory_path)
    for file_name, file_size in file_iterator:
        print(f"Файл: {file_name}, розмір файлу: {file_size}")
