import http

from django.shortcuts import render
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'base.html')


def send_form(request):
    if request.method == 'POST':
        form = Send(request.POST)
    else:
        form = Send()

    return render(request, 'send_form.html', {'form': form})
