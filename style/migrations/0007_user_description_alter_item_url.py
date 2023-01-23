# Generated by Django 4.1.5 on 2023-01-20 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0006_item_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.URLField(verbose_name='Реф. ссылка'),
        ),
    ]