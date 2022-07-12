from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

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
    a, b = int(a), int(b)
    if b == 0:
        c = {"a": a, "b": b, "operacja": "/", "wynik": "blad!!! Nie mozna dzielic przez 0."}
        return render(
            request=request,
            template_name="maths/operations.html",
            context=c)
    else:
        wynik = a / b
        c = {"a": a, "b": b, "operacja": "/", "wynik": wynik}
        return render(
            request=request,
            template_name="maths/operations.html",
            context=c)