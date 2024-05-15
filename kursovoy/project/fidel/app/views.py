from django.shortcuts import render
from app.models import Master
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    masters = Master.objects.all()[:4]
    return render(request, "index.html", {'masters': masters})

def masters(request):
    masters = Master.objects.all()
    sort_order = request.GET.get('sort', 'asc')
    if sort_order == 'desc':
        masters = Master.objects.all().order_by('-experience_years')
    else:
        masters = Master.objects.all().order_by('experience_years')

    paginator = Paginator(masters, 4)
    page = request.GET.get('page')
    
    try:
        masters = paginator.page(page)
    except PageNotAnInteger:
        masters = paginator.page(1)
    except EmptyPage:
        masters = paginator.page(paginator.num_pages)    
    return render(request, "masters.html", {'masters': masters, 'sort_order': sort_order})

def contacts(request):
    return render(request, "contacts.html")

def error(request):
    return render(request, "error.html")