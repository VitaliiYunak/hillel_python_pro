import subprocess
import os


def backup_mongodb(database_name, backup_dir):
    """
    Резервне копіювання бази даних
    :param database_name: назва БД
    :param backup_dir: директорія для резервної копії
    """
    backup_path = os.path.join(backup_dir, database_name)
    back_up = [
        'mongodump',
        '--db', database_name,
        '--out', backup_path
    ]

    try:
        subprocess.run(back_up, check=True)
        print(f"Копія бази даних '{database_name}' успішно створено в '{backup_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Помилка при створенні резервної копії: {e}")


if __name__ == "__main__":
    backup_mongodb("online", "/backup")
