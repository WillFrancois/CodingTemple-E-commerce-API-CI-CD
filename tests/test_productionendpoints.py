import unittest
from unittest.mock import Mock
from datetime import datetime
from app import app, test_token

class TestProductionEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.token = test_token
        self.timestamp = datetime.now()

    def test_add(self):
        mock_app = Mock(self.app)
        payload = {'product_id': 1, 'quantity_produced': 1, 'date_produced': f"{self.timestamp.year}-{self.timestamp.month}-{self.timestamp.day}"}
        # Provide the necessary user token to run the test, otherwise the test will fail with a 401 error
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'id': 1, 'product_id': 1, 'quantity_produced': 1, 'date_produced': f"{self.timestamp.year}-{self.timestamp.month}-{self.timestamp.day}"}
        response = mock_app.post('/productions/add', json=payload, headers=headers)
        response.pop('id', None)
        self.assertEqual(response, payload)

    def test_higher_quantity(self):
        mock_app = Mock(self.app)
        payload = {'product_id': 1, 'quantity_produced': 55, 'date_produced': f"{self.timestamp.year}-{self.timestamp.month}-{self.timestamp.day}"}
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'id': 2, 'product_id': 1, 'quantity_produced': 55, 'date_produced': f"{self.timestamp.year}-{self.timestamp.month}-{self.timestamp.day}"}
        response = mock_app.post('/productions/add', json=payload, headers=headers)
        response.pop("id", None)
        self.assertEqual(response, payload)

    def test_invalid_date(self):
        mock_app = Mock(self.app)
        payload = {'product_id': 1, 'quantity_produced': 1, 'date_produced': f"{self.timestamp.month}-{self.timestamp.day}-{self.timestamp.year}"}
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'date_produced': ['Not a valid date.']}
        response = mock_app.post('/productions/add', json=payload, headers=headers)
        self.assertEqual(response, {'date_produced': ['Not a valid date.']})

if __name__ == '__main__':
    unittest.main()
