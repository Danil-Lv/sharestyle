from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from .utils import make_slug


class User(AbstractUser):
    """Пользователь"""
    # прописать валидацию username
    username = models.CharField(max_length=150, unique=True, db_index=True)
    favorites = models.ManyToManyField('Style', blank=True, related_name='users_added', verbose_name='Избранное')
    subscriptions = models.ManyToManyField('self', verbose_name='Подписки', blank=True, symmetrical=False,
                                           related_name='subscribers')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='users_photo', blank=True)
    telegram = models.CharField(max_length=80, blank=True)
    instagram = models.URLField(max_length=80, blank=True)
    whatsapp = models.URLField(max_length=80, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    # slug

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'


class Style(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNISEX = 'U'
    GENDER_CHOICES = [
        (None, 'Выберите пол'),
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (UNISEX, 'Унисекс')
    ]

    title = models.CharField(max_length=80, verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='styles', editable=False)
    description = models.TextField(verbose_name='Описание', blank=True)
    items = models.ManyToManyField('Item', related_name='styles', verbose_name='Одежда')
    total_price = models.PositiveIntegerField(verbose_name='Цена')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    categories = models.ManyToManyField('Category', related_name='styles', verbose_name='Категории')
    tags = models.ManyToManyField('Tag', related_name='styles', verbose_name='Теги', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = make_slug(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('style', kwargs={'slug': self.request.slug})

    class Meta:
        verbose_name_plural = 'Стили'
        verbose_name = 'Стиль'


class Item(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNISEX = 'U'
    GENDER_CHOICES = [
        (None, 'Выберите пол'),
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (UNISEX, 'Унисекс')
    ]

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='items/%Y/%m/%d', verbose_name='Фото')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='clothes', null=True, verbose_name='Автор', editable=False)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    ref_url = models.URLField(verbose_name='Реф. ссылка')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = make_slug(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Вещи'
        verbose_name = 'Вещь'
        # ordering = ['-created_at'] # сортировка по умолчанию
