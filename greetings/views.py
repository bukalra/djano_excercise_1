from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def greetings(request, name):
    upper_name = f'Hello {name.capitalize()} !'
    return HttpResponse(upper_name)