# 9. Автоматичне резервне копіювання

import os
import shutil


class BackupFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.backup_name = f"{file_name}.bak"

    def __enter__(self):
        # Створюємо резервну копію файлу
        shutil.copy2(self.file_name, self.backup_name)
        return self.file_name

    def __exit__(self, except_type, except_val, exc_tb):
        if except_type is not None:
            # Якщо виникла помилка, відновлюємо резервну копію
            shutil.copy2(self.backup_name, self.file_name)
            print(f"Помилка: {except_val}. Відновлено резервну копію.")
        else:
            # Видаляємо резервну копію
            os.remove(self.backup_name)


if __name__ == "__main__":
    file_to_backup = "setting.json"

    try:
        with BackupFile(file_to_backup) as f:
            with open(f, 'r') as file:
                content = file.read()

            with open(f, 'w') as file:
                file.write(content + "\n")
    except Exception as e:
        print(f"Помилка: {e}")
