# Generated by Django 4.1.5 on 2023-01-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0009_rename_sex_item_gender_rename_sex_style_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=150, unique=True),
        ),
    ]