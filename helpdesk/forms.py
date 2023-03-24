from django import forms
from django.core.validators import RegexValidator


class Send(forms.Form):
    username = forms.CharField(label="Ваше имя", max_length=100)
    departament = forms.CharField(label="Ваш отдел", max_length=100)
    departament = forms.CharField(label="Ваш отдел", max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{12,12}$',  # Шаблон номера телефона
        message="Номер телефона должен быть данного формата : +79008007060"
    )
    phone_number = forms.CharField(label="Номер телефона", validators=[phone_regex])
