"""
Завдання 6. Приклад комплексного тестування
"""
import pytest


class BankAccount:
    """
    Поповнення рахунку, зняття коштів, поточний баланс.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount: float):
        """ Поповнення рахунку.
        """
        if amount <= 0:
            raise ValueError("Сума депозиту не може бути від\'ємною. ")
        self.balance += amount

    def withdraw(self, amount: float):
        """ Зняття коштів.
        """
        if amount <= 0:
            raise ValueError("Сума зняття має бути > 0.00")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів.")
        self.balance -= amount

    def get_balance(self) -> float:
        """Поточний баланс.
        """
        return self.balance


@pytest.fixture
def bank_account():
    """ Фікстура для створення об'єкта BankAccount.
    """
    bank_account = BankAccount()
    return bank_account


def test_deposit(bank_account):
    """Перевірка коректного поповнення рахунку.
    """
    bank_account.deposit(50.00)
    assert bank_account.get_balance() == 50.00


def test_withdraw(bank_account):
    """Перевірка зняття коштів.
    """
    bank_account.deposit(50.0)
    bank_account.withdraw(20.0)
    assert bank_account.get_balance() == 30.0


@pytest.mark.parametrize("amount, result_balance", [(50.0, 50.0), (200.0, 200.0)])
def test_deposit_parametrized(bank_account, amount, result_balance):
    """Перевірка поповнення рахунку з різними значеннями.
    """
    bank_account.deposit(amount)
    assert bank_account.get_balance() == result_balance


def test_withdraw_negative(bank_account):
    """Перевірка зняття негативної суми.
    """
    bank_account.deposit(50.0)
    with pytest.raises(ValueError, match="Сума зняття повинна бути > 0.00"):
        bank_account.withdraw(-20.0)
