"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

from http.client import responses
import json
import django
from django.test import TestCase

class ViewTest(TestCase):
    if django.VERSION[:2] >= (1, 7):

        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_titleinfo(self):
        response = self.client.get('/api/info?id=1')
        s = json.loads(response.content).items()
        for key, value in s:
            self.assertEqual(key, "code", response.content)
            break

    def test_title_list(self):
        response = self.client.get('/api/titles')
        s = json.loads(response.content).items()
        for key, value in s:
            self.assertEqual(key, "code")
            break

    def test_getvolume_list(self):
        response = self.client.get('/api/getvol?title_id=1')
        s = json.loads(response.content).items()
        for key, value in s:
            self.assertEqual(key, "code")
            break

    def test_chapter(self):
        response = self.client.get('/api/chapter?volume_id=1&page=1&page_size=1')
        s = json.loads(response.content).items()
        for key, value in s:
            self.assertEqual(key, "code", response.content)
            break

    def test_like(self):
        response = self.client.get('/api/like?chapter_id=1')
        s = json.loads(response.content).items()
        for key, value in s:
            self.assertEqual(key, "code")
            break
