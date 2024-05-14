from django.shortcuts import render
from .models import Master


def index(request):
    masters = Master.objects.all()[:4]
    return render(request, "index.html", {'masters': masters})

def masters(request):
    return render(request, "masters.html")

def contacts(request):
    return render(request, "contacts.html")