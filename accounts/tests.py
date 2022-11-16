from django.test import TestCase
from django.shortcuts import reverse


class TestAccounts(TestCase):
    def test_check_url_sing_up(self):
        res = self.client.get('/accounts/singup/')
        self.assertEqual(res.status_code, 200)

    def test_check_url_sing_up_with_name(self):
        res = self.client.get(reverse('singup'))
        self.assertEqual(res.status_code, 200)

    def test_check_url_login(self):
        res = self.client.get('/accounts/login/')
        self.assertEqual(res.status_code, 200)

    def test_check_url_login_with_name(self):
        res = self.client.get(reverse('login'))
        self.assertEqual(res.status_code, 200)
