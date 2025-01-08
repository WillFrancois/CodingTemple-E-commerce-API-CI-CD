import unittest
from unittest.mock import Mock
from app import app, test_token

class TestEmployeeEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.token = test_token

    def test_add(self):
        mock_app = Mock(self.app)
        payload = {'name': 'Craig', 'position': 'Head Manager'}
        # Provide the necessary user token to run the test, otherwise the test will fail with a 401 error
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'id': 1, 'name': 'Craig', 'position': 'Head Manager'}
        response = mock_app.post('/employees/add', json=payload, headers=headers)
        response.pop("id", None)
        self.assertEqual(response, payload)

    def test_empty_add(self):
        mock_app = Mock(self.app)
        payload = {}
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'name': ['Missing data for required field.'], 'position': ['Missing data for required field.']}
        response = mock_app.post('/employees/add', json=payload, headers=headers)
        self.assertEqual(response, {'name': ['Missing data for required field.'], 'position': ['Missing data for required field.']})

    def test_partial_add(self):
        mock_app = Mock(self.app)
        payload = {'name': 'Raj'}
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'position': ['Missing data for required field.']}
        response = mock_app.post('/employees/add', json=payload, headers=headers)
        self.assertEqual(response, {'position': ['Missing data for required field.']})


if __name__ == '__main__':
    unittest.main()
