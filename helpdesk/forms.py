from django import forms
from django.core.validators import RegexValidator


class FUser(forms.Form):
    phone_regex = RegexValidator(
        regex=r'^\+7\d{10}$',
        message="Номер телефона должен быть в формате: '+79008007766'"
    )
    username = forms.CharField(label="Ваше имя", max_length=100)
    departament = forms.CharField(label="Ваш отдел", max_length=100)
    phone_number = forms.CharField(label="Номер телефона", max_length=13, validators=[phone_regex])


class FTicket(forms.Form):
    list_choices = [('bug', 'Исправление багов'), ('buh', 'Помочь с документами')]
    choices = forms.ChoiceField(choices=list_choices, widget=forms.RadioSelect)
