from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TicketModel(models.Model):
    username = models.CharField(max_length=100, default='default_user')
    departament = models.CharField(max_length=100, default='default_departament')
    phone = models.CharField(max_length=13, default='default_phone')
    category = models.CharField(max_length=64, default='uncategorized')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
