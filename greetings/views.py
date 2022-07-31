from multiprocessing import context
from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def welcome(request):
    return render(
        request=request,
        template_name="greetings/main.html",
        context=None)   

def contact(request):
    return render(
        request=request,
        template_name="greetings/main.html",
        context=None)

def about(request):
    return render(
        request=request,
        template_name="greetings/main.html",
        context=None)