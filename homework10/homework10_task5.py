# Задача 5: паралельний пошук у файлах

import multiprocessing


def search_in_file(file_path, text):
    """
    Шукає текст у файлі.
    :param file_path: Шлях до файлу.
    :param text: Текст для пошуку.
    """
    found_lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if text in line:
                    found_lines.append(line.strip())
    except Exception as e:
        print(f"Не вдалося прочитати файл {file_path}: {e}")
    return file_path, found_lines


def parallel_search(text, files):
    """
    Паралельний пошук тексту у файлах.
    :param text: Текст для пошуку.
    :param files: Список файлів.
    """
    with multiprocessing.Pool(processes=len(files)) as res:
        results = res.starmap(search_in_file, [(file, text) for file in files])

    for file, lines in results:
        if lines:
            print(f"Текст '{text}' знайдено у файлі '{file}':")
            for line in lines:
                print(f" {line}")


if __name__ == "__main__":
    search_text = "PISA-2022"
    files_to_search = [
        "PISA_2022_Zvit_1.txt",
        "PISA_2022_Zvit_2.txt",
        "PISA_2022_Zvit_3.txt",
    ]
    parallel_search(search_text, files_to_search)
