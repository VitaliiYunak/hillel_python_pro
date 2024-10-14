"""
Завдання 2. Мокування за допомогою unittest.mock
"""
import requests
import unittest
from unittest.mock import Mock


class WebService:
    """
    Робить GET-запит та повертає JSON-відповідь
    """
    def get_data(self, url: str) -> dict:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


class TestWebService(unittest.TestCase):

    @unittest.mock.patch('requests.get')
    def test_success(self, mock_get):
        """Перевірка успішного запиту.
        """
        mock = Mock()
        mock.status_code = 200
        mock.json.return_value = {"data": "test"}
        mock_get.return_value = mock

        web_service = WebService()
        result = web_service.get_data('https://google.com')
        self.assertEqual(result, {"data": "test"})

    @unittest.mock.patch('requests.get')
    def test_not_found(self, mock_get):
        """Перевірка обробки помилки (404).
        """
        mock = Mock()
        mock.status_code = 404
        mock.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock

        web_service = WebService()
        with self.assertRaises(requests.exceptions.HTTPError):
            web_service.get_data('https://google.com')


if __name__ == '__main__':
    unittest.main()
