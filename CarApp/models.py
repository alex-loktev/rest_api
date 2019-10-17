from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    vim = models.CharField(max_length=60, db_index=True, verbose_name='VIM', unique=True)
    color = models.CharField(max_length=60, verbose_name='Цвет')
    brand = models.CharField(max_length=60, verbose_name='Марка')
    MODEL_CHOICES = [
        (1, 'Хэчбек'),
        (2, 'Седан'),
        (3, 'Внедорожник'),
        (4, 'Универсал'),
    ]
    model = models.CharField(max_length=60, choices=MODEL_CHOICES)
    owner = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
