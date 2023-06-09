# Generated by Django 4.2 on 2023-05-25 07:51

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_alter_objet_proprietaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='url_photo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='date_debut',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 25)), django.core.validators.MaxValueValidator(datetime.date(2023, 9, 2))]),
        ),
        migrations.AlterField(
            model_name='location',
            name='date_fin',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 25)), django.core.validators.MaxValueValidator(datetime.date(2023, 9, 2))]),
        ),
    ]
