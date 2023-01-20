from django.db import models
from django.contrib.auth import get_user_model
from .utils import make_slug
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User = get_user_model()

class User(AbstractUser):

    favorites = models.ManyToManyField('self', verbose_name='Подписки', blank=True, symmetrical=False, related_name='subscribes')

    image = models.ImageField(upload_to='users_photo')
    telegram = models.CharField(max_length=80, blank=True)
    instagram = models.CharField(max_length=80, blank=True)
    whatsapp = models.CharField(max_length=80, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'


class Style(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNISEX = 'U'
    SEX_CHOICES = [
        (None, 'Выберите пол'),
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (UNISEX, 'Унисекс')
    ]

    title = models.CharField(max_length=80, verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='styles')
    description = models.TextField(verbose_name='Описание', blank=True)
    items = models.ManyToManyField('Item', related_name='styles', verbose_name='Одежда')
    total_price = models.PositiveIntegerField(verbose_name='Цена')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    categories = models.ManyToManyField('Category', related_name='styles', verbose_name='Категории')
    tags = models.ManyToManyField('Tag', related_name='styles', verbose_name='Теги', blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name='Пол')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Стили'
        verbose_name = 'Стиль'


class Item(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNISEX = 'U'
    SEX_CHOICES = [
        (None, 'Выберите пол'),
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (UNISEX, 'Унисекс')
    ]

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='items/%Y/%m/%d', verbose_name='Фото')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name='Пол')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='clothes', null=True, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    # URl

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Вещи'
        verbose_name = 'Вещь'
        # ordering = ['-created_at'] # сортировка по умолчанию
