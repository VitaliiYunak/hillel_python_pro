# 7. Парсинг великих лог-файлів для аналітики

def error_log(file_name):
    """
    Генератор, що зчитує лог-файл і повертає лише рядки з помилками.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if ' 4' in line or ' 5' in line:
                yield line.strip()


def save_error_logs(input_file, output_file):
    """
    Зберігає рядки з помилками у новий файл.
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in error_log(input_file):
            outfile.write(line + '\n')


if __name__ == "__main__":
    save_error_logs("web_log.txt", "web_log_new.txt")
