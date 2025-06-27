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

    def test_curriculum_loads(self):
        response = self.client.get(reverse('curriculum'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)


class ChatMessageTest(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        self.user = User.objects.create_user(username='testuser', password='pass')

    def test_chat_creates_message(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post(reverse('chat'), {'message': 'hello'})
        self.assertEqual(response.status_code, 200)
        from .models import ChatMessage
        self.assertEqual(ChatMessage.objects.filter(user=self.user).count(), 1)
