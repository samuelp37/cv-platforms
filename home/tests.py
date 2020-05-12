from django.test import TestCase

# Testing home page accessibility
class TestHome(TestCase):
    def test_home(self):
        resp = self.client.get('/public/')
        self.assertEqual(resp.status_code, 200)