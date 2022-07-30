from django.test import TestCase
from posts.models import Post, Author

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title='first', content='test')

    def test_result_str(self):
        p1 = Post.objects.get(id=1)
        self.assertEqual(str(p1), "id:1, title=first, content=test")

class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick='radek', email='bukalskiradek@gmail.com')
                

    def test_result_str(self):
        a1 = Author.objects.get(nick='radek')
        self.assertEqual(str(a1), "nick=radek, email=bukalskiradek@gmail.com")
        

