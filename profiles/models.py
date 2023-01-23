from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class User(AbstractUser):
    """Пользователь"""
    username = models.CharField(max_length=150, unique=True, db_index=True, validators=[
        RegexValidator(
            regex=r"\W|[А-яё]",
            message='Допустимые символы: _A-z0-9',
            inverse_match=True
        ), RegexValidator(
            regex=r"^\d",
            message='Логин должен начинаться с буквы',
            inverse_match=True
        )
    ])
    favorites = models.ManyToManyField('style.Style', blank=True, related_name='users_added', verbose_name='Избранное')
    subscriptions = models.ManyToManyField('self', verbose_name='Подписки', blank=True, symmetrical=False,
                                           related_name='subscribers')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='users_photo', blank=True)
    telegram = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    whatsapp = models.CharField(max_length=500, blank=True, validators=[
        RegexValidator(
            regex=r"[^0-9+]+",
            message='Неправильно введен номер Whatsapp',
            inverse_match=True
        )
    ])
