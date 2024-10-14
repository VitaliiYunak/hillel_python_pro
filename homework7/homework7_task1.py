"""
Завдання 1. Модульне тестування з використанням unittest
"""
import unittest


class StringProcessor:
    """
    Повертає перевернутий рядок.
    Робить першу літеру рядка великої.
    Повертає кількість голосних у рядку.
    """
    def reverse_string(self, s: str) -> str:
        """
        Повертає перевернутий рядок
        """
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """
        Робить першу літеру рядка великої.
        """
        return s.capitalize()

    def count_vowels(self, s: str) -> int:
        """
        Повертає кількість голосних у рядку.
        """
        vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count


class TestStringProcessor(unittest.TestCase):
    """
    Тести для кожного методу, перевіряючи кілька різних сценаріїв
    """

    def setUp(self):
        self.test = StringProcessor()

    @unittest.skip("Пропускаємо тест 'test_reverse_string_empty' для порожнього рядка")
    def test_reverse_string_empty(self):
        self.assertEqual(self.test.reverse_string(""), "")

    def test_reverse_string(self):
        """Перевіряє, чи є рядок перевернутим.
        """
        self.assertEqual(self.test.reverse_string("hello, word"), "drow ,olleh")
        self.assertEqual(self.test.reverse_string("Hello, word"), "drow ,olleH")
        self.assertEqual(self.test.reverse_string("1234!@#"), "#@!4321")
        self.assertEqual(self.test.reverse_string(""), "")

    def test_capitalize_string(self):
        """Перевіряє, чи перша літера рядка велика.
        """
        self.assertEqual(self.test.capitalize_string("hello world"), "Hello world")
        self.assertEqual(self.test.capitalize_string("Hello World"), "Hello world")
        self.assertEqual(self.test.capitalize_string("1234!@#"), "1234!@#")
        self.assertEqual(self.test.capitalize_string(""), "")

    def test_count_vowels(self):
        """Перевіряє кількість голосних у рядку.
        """
        self.assertEqual(self.test.count_vowels("Привіт, світе!"), 4)
        self.assertEqual(self.test.count_vowels("ПрИвІт, свІтЕ!"), 4)
        self.assertEqual(self.test.count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
