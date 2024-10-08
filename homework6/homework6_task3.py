# Завдання 3: Робота з CSV файлами
import csv


def add_student(file_name, name, age, rating):
    """
    Додавання нового студента до файлу
    :param file_name: назва файлу
    :param name: імя студента
    :param age: вік
    :param rating: оцінка
    """
    with open(file_name, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, rating])


def read_students(file_name):
    """
    Читання даних з CSV-файлу
    :param file_name: назва файлу
    :return: список студентів
    """
    students = []
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            students.append(row)
    return students


def average_rating(students):
    """
    Обчислення середньої оцінки
    """
    total_rating = 0
    for student in students:
        total_rating += int(student[2])
    rating = total_rating / len(students) if students else 0
    return rating


if __name__ == "__main__":
    csv_file = "students.csv"
    # Додаємо нового студента
    new_name = input("Введіть ім'я нового студента: ")
    new_age = input("Введіть вік нового студента: ")
    new_rating = input("Введіть оцінку нового студента: ")
    add_student(csv_file, new_name, new_age, new_rating)
    print(f"Студент {new_name} доданий.")

    # Читаємо дані з файлу
    students = read_students(csv_file)
    print(students)

    # Середня оцінка студентів
    print(f"Середня оцінка студентів: {average_rating(students):.2f}")
