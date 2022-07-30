from django.test import TestCase, Client
from posts.models import Post, Author
class PostViewsTest(TestCase):

    def setUp(self):
        Post.objects.create(title='new post', content='new post content')
        Post.objects.create(title='new post 2', content='new post content 2')
        Post.objects.create(title='new post 3', content='new post content 3')
        Post.objects.create(title='new post 4', content='new post content 4')

        self.client = Client()

    def test_posts_list(self):
        response = self.client.get("/posts/posts_list/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 4)
        

        self.assertIn('<li><a href="/posts/posts/1">id:1, title=new post, content=new post content</a></li>', response.content.decode())
        self.assertIn('<li><a href="/posts/posts/2">id:2, title=new post 2, content=new post content 2</a></li>', response.content.decode())
        self.assertIn('<li><a href="/posts/posts/3">id:3, title=new post 3, content=new post content 3</a></li>', response.content.decode())
        self.assertIn('<li><a href="/posts/posts/4">id:4, title=new post 4, content=new post content 4</a></li>', response.content.decode())

class AuthorViewsTest(TestCase):

    def setUp(self):
        Author.objects.create(nick='radek', email='bukalskiradek@gmail.com')
        Author.objects.create(nick='adrian', email='adrina@gmail.com')
        Author.objects.create(nick='darek', email='darek@gmail.com')
        Author.objects.create(nick='szymon', email='szymon@gmail.com')


        self.client = Client()

    def test_authors_list(self):
        response = self.client.get("/posts/authors_list/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["authors"]), 4)
        

        self.assertIn('<li><a href="/posts/author_details/1">nick=radek, email=bukalskiradek@gmail.com</a></li>', response.content.decode())
        self.assertIn('<li><a href="/posts/author_details/2">nick=adrian, email=adrina@gmail.com</a></li>', response.content.decode())
        self.assertIn('<li><a href="/posts/author_details/3">nick=darek, email=darek@gmail.com</a></li>', response.content.decode())
        self.assertIn('<li><a href="/posts/author_details/4">nick=szymon, email=szymon@gmail.com</a></li>', response.content.decode())
