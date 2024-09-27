# 6. Access-like
import re


class User:
    """
    Використовуючи  @property встановлює та змінює інформацію про користувача: прізвище, ім'я,
    електронна адреса. Перевіряє коректність введення  електронної адреси.
    """
    def __init__(self, last_name, first_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    # Отримання та встановлення прізвища
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Необхідно ввести прізвище")
        self.__last_name = value

    # Отримання та встановлення імені
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("Необхідно ввести ім'я")
        self.__first_name = value

    # Отримання та встановлення електронної пошти
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not self.valid_email(value):
            raise ValueError("Неправильний формат електронної пошти")
        self.__email = value

    # Перевірка формату електронної пошти
    @staticmethod
    def valid_email(email):
        valid_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        result = re.match(valid_email, email)
        return result

    def __str__(self):
        return f"Користувач: {self.last_name} {self.first_name}, email:{self.email}"


user = User("Мельник", "Андрій", "a.melnik@gmail.com")
print(user)
print(f"Прізвище: {user.last_name}")
print(f"Ім'я: {user.first_name}")
try:
    user.last_name = "Мельничук"
    user.email = "a.melnichuk@gmail.com"
    print("Інформація про користувача після змін:")
    print(user)
    new_email = "email@лрвавп.com"
    user.email = new_email
except ValueError as e:
    print(f"Помилка: {new_email} - {e}")
