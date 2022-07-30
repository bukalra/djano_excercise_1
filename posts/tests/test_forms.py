from posts.forms import PostForm, AuthorForm
from django.test import TestCase

# Create your tests here.
from posts.models import Post, Author


class PostFormTest(TestCase):

    def test_post_save_correct_data(self):
        data = {"title": "new post", "content": "new post content", "author_id_id":1}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Post)
        self.assertEqual(r.title, "new post")
        self.assertIsNotNone(r.id)

class AuthoeFormTest(TestCase):

    def test_post_save_correct_data(self):
        data = {"nick": "radek", "email": "bukalskiradek@gmail.com"}
        self.assertEqual(len(Author.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Author)
        self.assertEqual(r.nick, "radek")
        self.assertIsNotNone(r.id)