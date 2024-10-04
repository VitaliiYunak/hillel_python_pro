# 4. Генератор для обробки великих файлів

def filter_lines(file_name, keyword):
    """
    Генератор, який фільтрує рядки з файлу за ключовим словом.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        for row in file:
            if keyword in row:
                yield row.strip()


def save_filtered_lines(input_name, output_name, keyword):
    """
    Зберігає відфільтровані рядки у новий файл.
    """
    with open(output_name, 'w', encoding='utf-8') as outfile:
        for line in filter_lines(input_name, keyword):
            outfile.write(line + '\n')
    print(f"Ключеве слово: {keyword}")
    print(f"Новий файл: {output_name}")


if __name__ == "__main__":
    save_filtered_lines('log.txt', 'log_new.txt', 'SUCSSES')
