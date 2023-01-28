from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


class User(AbstractUser):
    """Пользователь"""
    username = models.CharField(max_length=150, unique=True,)
    favorites = models.ManyToManyField('style.Style', blank=True, null=True, related_name='users_added',
                                       verbose_name='Избранное')
    subscriptions = models.ManyToManyField('self', verbose_name='Подписки', blank=True, symmetrical=False,
                                           related_name='subscribers',)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='users_photo', blank=True, null=True)
    telegram = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    whatsapp = models.CharField(max_length=500, blank=True, validators=[
        RegexValidator(
            regex=r"[^0-9+]+",
            message='Неправильно введен номер Whatsapp',
            inverse_match=True
        )
    ])
    is_stylist = models.BooleanField(default=False, verbose_name='Стилист')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # def clean(self):
    #     # errors = {}
    #
    #     if self.type == 'S' and self.first_name == '':
    #         raise ValidationError('Поля "Имя" обязательно к заполнению')
    #
    #     if self.type == 'S' and not self.description:
    #         raise ValidationError('Поле "О себе" обязательно к заполнению')

    # if self.username == self.username.upper():
    #     errors['username'] = ValidationError(f'Логин большими буквами')
    #
    # if 'q' in self.description:
    #     errors['description'] = ValidationError(f'Логин большими буквами')

    # if errors:
    #     errors[NON_FIELD_ERRORS] = 'ошибка в модели'
    #     raise ValidationError(errors)
