# Generated by Django 4.1.5 on 2023-01-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='users_photo'),
        ),
    ]