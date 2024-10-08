# Завдання 4: Робота з JSON
import json


def load_books(filename):
    """
    Завантаження JSON-файлу
    :param filename: назва файлу
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def print_available_books(books):
    """
    Виведення доступних книг
    """
    available_books = [book for book in books if book["наявність"]]
    if available_books:
        print("Доступні книги:")
        for book in available_books:
            print(f"{book['назва']} автор: {book['автор']}, рік: {book['рік']}")
    else:
        print("Немає доступних книг.")


def add_book(filename, new_book):
    """
    Додавання нової книги
    :param filename: назва файлу
    :param new_book: інформація про нову книгу
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        books = json.load(file)
        books.append(new_book)
        file.seek(0)
        json.dump(books, file, ensure_ascii=False, indent=4)
        file.truncate()


if __name__ == "__main__":
    filename = 'books.json'

    # Завантаження книги
    books = load_books(filename)
    print(books)

    # Доступні книги
    print_available_books(books)

    # Додавання нової книги
    new_book = {
        "назва": "Книга 3",
        "автор": "Автор 3",
        "рік": 2024,
        "наявність": True
    }
    add_book(filename, new_book)
