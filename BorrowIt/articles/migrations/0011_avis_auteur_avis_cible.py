# Generated by Django 4.2 on 2023-05-09 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_remove_avis_auteur_location_emprunteur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avis',
            name='auteur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='auteur', to='articles.utilisateur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='avis',
            name='cible',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cible', to='articles.utilisateur'),
            preserve_default=False,
        ),
    ]
