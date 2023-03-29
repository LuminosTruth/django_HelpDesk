import http

from django.shortcuts import render
from .models import *
from .forms import *


def send_form(request):
    if request.method == 'POST':
        user_form = FUser(request.POST)
        ticket_form = FTicket(request.POST)
        if user_form.is_valid() and ticket_form.is_valid():
            new_user = TicketModel(
                username=user_form.cleaned_data['username'],
                departament=user_form.cleaned_data['departament'],
                phone=user_form.cleaned_data['phone_number'],
                category=ticket_form.cleaned_data['choices']
            )
            new_user.save()
    else:
        user_form = FUser()
        ticket_form = FTicket()
    return render(request, 'send_form.html', {'user_form': user_form, 'ticket_form': ticket_form})
