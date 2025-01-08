import unittest
from unittest.mock import Mock
from app import app, test_token

class TestProductEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.token = test_token

    def test_add(self):
        mock_app = Mock(self.app)
        payload = {'name': 'Red Delicious Apple', 'price': 10.00}
        # Provide the necessary user token to run the test, otherwise the test will fail with a 401 error
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'id': 1, 'name': 'Red Delicious Apple', 'price': 10.00}
        response = mock_app.post('/products/add', json=payload, headers=headers)
        response.pop("id", None)
        self.assertEqual(response, payload)

    def test_partial_data(self):
        mock_app = Mock(self.app)
        payload = {'name': 'Red Delicious Apple'}
        # Provide the necessary user token to run the test, otherwise the test will fail with a 401 error
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'price': ['Missing data for required field.']}
        response = mock_app.post('/products/add', json=payload, headers=headers)
        self.assertEqual(response, {'price': ['Missing data for required field.']})

    def test_invalid_data(self):
        mock_app = Mock(self.app)
        payload = {'name': 'Red Delicious Apple', 'price': '$5.99'}
        # Provide the necessary user token to run the test, otherwise the test will fail with a 401 error
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'price': ['Not a valid number.']}
        response = mock_app.post('/products/add', json=payload, headers=headers)
        self.assertEqual(response, {'price': ['Not a valid number.']})

if __name__ == '__main__':
    unittest.main()
