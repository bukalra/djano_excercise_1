from django.contrib import admin
from django.urls import path
from .views import add, sub, mul, div, math

urlpatterns = [
    path('', math),
    path('add/<int:a>/<int:b>', add),
    path('sub/<int:a>/<int:b>', sub),
    path('mul/<int:a>/<int:b>', mul),
    path('div/<int:a>/<int:b>', div),
]
