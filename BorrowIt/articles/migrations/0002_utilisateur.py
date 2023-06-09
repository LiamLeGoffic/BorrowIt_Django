# Generated by Django 4.2 on 2023-05-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('numero_tel', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=50)),
                ('mot_de_passe', models.CharField(max_length=50)),
                ('date_creation', models.DateField(null=True)),
            ],
        ),
    ]
