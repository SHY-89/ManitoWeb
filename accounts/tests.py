from django.test import TestCase, Client
from django.urls import reverse

class SocialLoginTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_kakao_login(self):
        response = self.client.get(reverse('socialaccount_login', args=['kakao']))
        self.assertEqual(response.status_code, 302)  # 리다이렉트 확인

    def test_login_redirect(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # 홈 페이지 접근 확인