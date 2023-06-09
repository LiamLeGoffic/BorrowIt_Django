# Generated by Django 4.2 on 2023-05-25 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_alter_location_emprunteur_alter_location_objet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avis',
            name='auteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auteur_avis', to='articles.utilisateur'),
        ),
        migrations.AlterField(
            model_name='avis',
            name='cible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cible_avis', to='articles.utilisateur'),
        ),
    ]
