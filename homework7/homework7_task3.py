"""Завдання 3. Використання фікстур у pytest
"""

import pytest


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name: str, age: int):
        """Додає користувача до списку.
        """
        self.users.append({'name': name, 'age': age})

    def remove_user(self, name: str):
        """Видаляє користувача по імені.
        """
        new_users = []
        for user in self.users:
            if user['name'] != name:
                new_users.append(user)
        self.users = new_users

    def get_all_users(self):
        """ Список усіх користувачів.
        """
        return self.users


@pytest.fixture
def user_manager():
    """Додає користувачів для використання в тестах.
    """
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


def test_add_user(user_manager):
    """ Перевіряє, що новий користувач правильно додається.
    """
    user_manager.add_user("Mike", 22)
    assert user_manager.get_all_users()[-1] == {'name': 'Mike', 'age': 22}


def test_remove_user(user_manager):
    """ Перевіряє, що користувач видаляється правильно.
    """
    user_manager.remove_user("Alice")
    assert user_manager.get_all_users()[0] == {'name': 'Bob', 'age': 25}


def test_get_all_users(user_manager):
    """ Перевіряє, що всі користувачі правильні.
    """
    users = user_manager.get_all_users()
    assert users[0] == {'name': 'Alice', 'age': 30}
    assert users[1] == {'name': 'Bob', 'age': 25}


def test_skip(user_manager):
    """ Тест пропускається, якщо менше трьох користувачів.
    """
    user_manager.remove_user("Alice")
    user_manager.remove_user("Bob")

    if len(user_manager.get_all_users()) < 3:
        pytest.skip("Для цього тесту повинно бути більше трьох користувачів.")


if __name__ == "__main__":
    pytest.main()
