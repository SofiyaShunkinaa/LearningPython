from django.http import HttpResponse, HttpResponsePermanentRedirect


def index(request):
    return HttpResponse("<h2>Главная</h2>", headers={'secret code': 'testing'})


def about(request):
    return HttpResponse("<h2>О нас</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def user(request):
    name = request.GET.get('name', "Undefined")
    age = request.GET.get('age', 0)
    return HttpResponse(f"<h2>Name: {name}, age: {age}</h2>")


def details(requets):
    return HttpResponsePermanentRedirect("/")
