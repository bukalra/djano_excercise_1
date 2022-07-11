from django.contrib import admin
from django.urls import path
from .views import greetings

urlpatterns = [
    path('<name>', greetings)
]
