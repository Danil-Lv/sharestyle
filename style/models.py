from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CheckConstraint, Q, UniqueConstraint

from profiles.models import User
from .utils import make_slug



class Category(models.Model):
    """Категория"""
    title = models.CharField(max_length=50, unique=True)
    # slug

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Tag(models.Model):
    """Тег"""
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'


class Style(models.Model):
    """Стиль"""
    MALE = 'M'
    FEMALE = 'F'
    UNISEX = 'U'
    GENDER_CHOICES = [
        (None, 'Выберите пол'),
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (UNISEX, 'Унисекс')
    ]

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='styles')
    description = models.TextField(verbose_name='Описание', blank=True)
    items = models.ManyToManyField('Item', related_name='styles', verbose_name='Одежда')
    total_price = models.PositiveIntegerField(verbose_name='Цена')
    slug = models.SlugField(unique=True, verbose_name='Ссылка', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    categories = models.ManyToManyField('Category', related_name='styles', verbose_name='Категории')
    tags = models.ManyToManyField('Tag', related_name='styles', verbose_name='Теги', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = make_slug(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Стили'
        verbose_name = 'Стиль'



class Item(models.Model):
    """Вещь"""
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
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='clothes', null=True, verbose_name='Автор',
                               editable=False)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(verbose_name='Ссылка', blank=True, unique=True)
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
        get_latest_by = 'created_at'
        # constraints = [
        #     CheckConstraint(check=Q(price__lte=1000), name='price_constraint', violation_error_message='Прайс высокий'),
        #     UniqueConstraint(fields=('title', 'price'), name='title_price_constraint', violation_error_message='Поля меняй')
        # ]

        # ordering = ['-created_at'] # сортировка по умолчанию


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reviews', verbose_name='Пользователь', null=True , blank=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name='reviews', verbose_name='Стиль', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author} - {self.style}'