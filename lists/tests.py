from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# for initial test django TestCase
#
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):

    def test_uses_home_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': '신규 작업 아이템'})
        self.assertIn('신규 작업 아이템', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
