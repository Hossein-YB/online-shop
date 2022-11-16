from django.test import TestCase
from django.shortcuts import reverse


class HomePageTest(TestCase):
    def test_home_page_url(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_home_page_url_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_about_us_url(self):
        res = self.client.get('/aboutus/')
        self.assertEqual(res.status_code, 200)

    def test_about_us_url_name(self):
        res = self.client.get(reverse('about_us'))
        self.assertEqual(res.status_code, 200)
