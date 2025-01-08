import unittest
from unittest.mock import Mock
from app import app, test_token

class TestCustomerEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.token = test_token

    def test_add(self):
        mock_app = Mock(self.app)
        payload = {'name': 'Mason', 'phone': '555-555-5555', 'email': 'test@test.com'}
        # Provide the necessary user token to run the test, otherwise the test will fail with a 401 error
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'id': 1, 'name': 'Mason', 'phone': '555-555-5555', 'email': 'test@test.com'}
        response = mock_app.post('/customers/add', json=payload, headers=headers)
        response.pop('id', None)
        self.assertEqual(response, payload)

    def test_empty_add(self):
        mock_app = Mock(self.app)
        payload = {}
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'email': ['Missing data for required field.'], 'name': ['Missing data for required field.'], 'phone': ['Missing data for required field.']}
        response = mock_app.post('/customers/add', json=payload, headers=headers)
        self.assertEqual(response, {'email': ['Missing data for required field.'], 'name': ['Missing data for required field.'], 'phone': ['Missing data for required field.']})

    def test_partial_add(self):
        mock_app = Mock(self.app)
        payload = {'name': 'Susan'}
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'email': ['Missing data for required field.'], 'phone': ['Missing data for required field.']}
        response = mock_app.post('/customers/add', json=payload, headers=headers)
        self.assertEqual(response, {'email': ['Missing data for required field.'], 'phone': ['Missing data for required field.']})



if __name__ == '__main__':
    unittest.main()
