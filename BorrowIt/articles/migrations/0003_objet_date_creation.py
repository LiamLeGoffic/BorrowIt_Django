# Generated by Django 4.2 on 2023-05-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='objet',
            name='date_creation',
            field=models.DateField(null=True),
        ),
    ]
