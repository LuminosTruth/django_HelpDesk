from django import forms
from django.core.validators import RegexValidator


class FUser(forms.Form):
    username = forms.CharField(label="Ваше имя", max_length=100)
    departament = forms.CharField(label="Ваш отдел", max_length=100)
    phone_number = forms.CharField(label="Номер телефона", max_length=13)


class FTicket(forms.Form):
    list_choices = [('bug1', 'Исправление багов'), ('bug2', 'Исправление багов')]
    choices = forms.ChoiceField(choices=list_choices, widget=forms.RadioSelect)
