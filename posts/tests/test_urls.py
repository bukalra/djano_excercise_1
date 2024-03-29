from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from posts.views import posts_details, posts_list, authors_list, author_details

class TestUrls(TestCase):
    def test_resolution_for_posts_list(self):
        resolver = resolve('/posts/posts_list/')
        self.assertEqual(resolver.func, posts_list)

    def test_resolution_for_post_details(self):
        resolver = resolve('/posts/posts/1')
        self.assertEqual(resolver.func, posts_details)

    def test_resolution_for_author_list(self):
        resolver = resolve('/posts/authors_list/')
        self.assertEqual(resolver.func, authors_list)

    def test_resolution_for_author_details(self):
        resolver = resolve('/posts/author_details/1')
        self.assertEqual(resolver.func, author_details)