from django.contrib import admin
from django.urls import path
from .views import posts_list, posts_details, authors_list, author_details

app_name="posts"
urlpatterns = [
    path('posts_list/', posts_list, name='posts_list'),   
    path('posts/<int:id>', posts_details, name='posts_details'),
    path('authors_list/', authors_list, name='authors_list'),   
    path('author_details/<int:id>', author_details, name='author_details'),
]