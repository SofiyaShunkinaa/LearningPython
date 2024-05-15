from django import forms
from .models import Service, Master
from datetime import date


class AppointmentForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label='Выберите услугу')
    master = forms.ModelChoiceField(queryset=Master.objects.all(), label='Выберите мастера')
    date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=15, label='Номер телефона')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number

    def clean_date(self):
        date_value = self.cleaned_data['date']
        if date_value < date.today():
            raise forms.ValidationError("Выберите корректную дату в будущем.")
        return date_value
