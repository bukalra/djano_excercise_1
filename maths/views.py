from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
def math(request):
    return HttpResponse("Tu będzie matma")

def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik}
    #    return HttpResponse(t.render(c))
    return render(
        request=request,
        template_name="maths/operations.html",
        context=c)

def sub(request, a, b):
    wynik = a - b
    c = {"a": a, "b": b, "operacja": "-", "wynik": wynik}
    return render(
        request=request,
        template_name="maths/operations.html",
        context=c)

def mul(request, a, b):
    a, b = int(a), int(b)
    wynik = a * b
    c = {"a": a, "b": b, "operacja": "*", "wynik": wynik}
    return render(
        request=request,
        template_name="maths/operations.html",
        context=c)

def div(request, a, b):
    if int(b) == 0:
        wynik = "Error"
        messages.add_message(request, messages.ERROR, "Dzielenie przez zero!")
    else:
        wynik = a / int(b)
    c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
    return render(
        request=request,
        template_name="maths/operations.html",
        context=c)