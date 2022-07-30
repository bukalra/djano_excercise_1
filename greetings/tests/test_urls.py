from unittest import TestCase
from django.urls import resolve
from greetings.views import greetings

class TestUrls2(TestCase):
    def test_greetings(self):
        resolver = resolve('/greetings/radek')
        self.assertEqual(resolver.func, greetings)

