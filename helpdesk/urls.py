from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', send_form, name='send-form'),
    path('send_succes/', send_success, name='send-success'),
]
