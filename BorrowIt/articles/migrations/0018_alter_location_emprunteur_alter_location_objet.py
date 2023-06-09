# Generated by Django 4.2 on 2023-05-25 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_utilisateur_url_photo_alter_location_date_debut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='emprunteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.utilisateur'),
        ),
        migrations.AlterField(
            model_name='location',
            name='objet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.objet'),
        ),
    ]
