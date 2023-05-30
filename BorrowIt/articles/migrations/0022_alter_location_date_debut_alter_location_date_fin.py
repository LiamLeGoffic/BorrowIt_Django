# Generated by Django 4.2 on 2023-05-26 13:08

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0021_alter_location_date_debut_alter_location_date_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='date_debut',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 2, 15)), django.core.validators.MaxValueValidator(datetime.date(2023, 9, 3))]),
        ),
        migrations.AlterField(
            model_name='location',
            name='date_fin',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 2, 15)), django.core.validators.MaxValueValidator(datetime.date(2023, 9, 3))]),
        ),
    ]