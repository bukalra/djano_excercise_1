from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(
    'posts.Author',
    on_delete=models.CASCADE,
    null=True,
    blank=True)

    def __str__(self):
        return f"id:{self.id}, title={self.title}, content={self.content}"

class Author(models.Model):
    nick = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"nick={self.nick}, email={self.email}"