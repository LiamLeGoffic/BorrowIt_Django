# Generated by Django 4.2 on 2023-05-23 07:52

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_alter_abonnement_client_alter_location_date_debut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='date_debut',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 23)), django.core.validators.MaxValueValidator(datetime.date(2023, 8, 31))]),
        ),
        migrations.AlterField(
            model_name='location',
            name='date_fin',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 23)), django.core.validators.MaxValueValidator(datetime.date(2023, 8, 31))]),
        ),
    ]
