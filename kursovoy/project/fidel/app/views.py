from django.shortcuts import render
from app.models import Master, Appointment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AppointmentForm


def index(request):
    masters = Master.objects.all()[:4]
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = Appointment(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                service=form.cleaned_data['service'],
                master=form.cleaned_data['master'],
                date=form.cleaned_data['date'],
                phone_number=form.cleaned_data['phone_number']
            )
            appointment.save()
            print("Новая запись создана:")
            print("Имя:", appointment.first_name)
            print("Фамилия:", appointment.last_name)
            print("Дата:", appointment.date)
            print("Услуга:", appointment.service)
            print("Мастер:", appointment.master)
            print("Номер телефона:", appointment.phone_number)
            return render(request, 'index.html', {'masters': masters,'form': form, 'success': True})
    else:
        form = AppointmentForm()
    return render(request, "index.html", {'masters': masters, 'form': form})

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

