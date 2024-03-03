from django.http import HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>О нас</h2>")


def contact(request):
    return JsonResponse({"name":"Tom", "age": 20})


def user(request):
    name = request.GET.get('name', "Undefined")
    age = request.GET.get('age', 0)
    return HttpResponse(f"<h2>Name: {name}, age: {age}</h2>")


def details(requets):
    return HttpResponsePermanentRedirect("/")
