import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>', response.data)  # Check if the response contains a paragraph tag

    def test_tweet_route(self):
        response = self.app.post('/tweet', data={'sentence': 'Test sentence'})
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect

if __name__ == '__main__':
    unittest.main()