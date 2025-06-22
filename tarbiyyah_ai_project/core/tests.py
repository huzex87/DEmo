from django.test import TestCase
from django.urls import reverse


class BasicPagesTest(TestCase):
    def test_index_loads(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_signup_loads(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_login_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
