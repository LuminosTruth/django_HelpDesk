import http

from django.shortcuts import render, redirect
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
            return redirect('send-success')
    else:
        user_form = FUser()
        ticket_form = FTicket()
    return render(request, 'send_form.html', {'user_form': user_form, 'ticket_form': ticket_form})


def send_success(request):
    return render(request, 'send_success.html')


def tickets(request):
    return render(request, 'tickets.html', {'tickets': TicketModel.objects.all()})
