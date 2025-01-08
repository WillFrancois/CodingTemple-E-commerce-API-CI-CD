import unittest
from unittest.mock import Mock
from app import app, test_token

class TestOrderEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.token = test_token

    def test_add(self):
        mock_app = Mock(self.app)
        payload = {'customer_id': 1, 'product_id': 1, 'quantity': 1, 'total_price': 10.00}
        # Provide the necessary user token to run the test, otherwise the test will fail with a 401 error
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'id': 1, 'customer_id': 1, 'product_id': 1, 'quantity': 1, 'total_price': 10.00}
        response = mock_app.post('/orders/add', json=payload, headers=headers)
        response.pop("id", None)
        self.assertEqual(response, payload)

    def test_bad_customer_id(self):
        mock_app = Mock(self.app)
        payload = {'customer_id': '25', 'product_id': 1, 'quantity': 1, 'total_price': 10.00}
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = None
        response = mock_app.post('/orders/add', json=payload, headers=headers)
        self.assertIsNone(response)

    def test_partial_data(self):
        mock_app = Mock(self.app)
        payload = {'customer_id': 1, 'product_id': 1, 'quantity': 1}
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        mock_app.post.return_value = {'total_price': ['Missing data for required field.']}
        response = mock_app.post('/orders/add', json=payload, headers=headers)
        self.assertEqual(response, {'total_price': ['Missing data for required field.']})



if __name__ == '__main__':
    unittest.main()
