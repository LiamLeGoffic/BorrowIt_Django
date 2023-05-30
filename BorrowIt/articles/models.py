from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, timedelta
from django.db import models


class Utilisateur(models.Model):

    prenom = models.fields.CharField(max_length=50)
    nom = models.fields.CharField(max_length=50)
    numero_tel = models.fields.CharField(max_length=10)
    mail = models.fields.EmailField(max_length=50)
    url_photo = models.fields.URLField(null=True, blank=True)
    mot_de_passe = models.fields.CharField(max_length=50)
    date_creation = models.fields.DateField(auto_now_add=True)


class Objet(models.Model):

    class Tag(models.TextChoices):
        OUTIL = 'O'
        FILM = 'F'
        LIVRE = 'L'
        JEU = 'J'
        INFORMATIQUE = 'IF'
        VEHICULE = 'V'
        MODE = 'MO'
        IMMOBILIER = 'IM'
        MUSIQUE = 'MU'
        AUTRE = 'A'

    nom = models.fields.CharField(max_length=100)
    url_photo = models.fields.URLField(null=True, blank=True)
    description = models.fields.CharField(max_length=500, null=True, blank=True)
    prix_jour = models.fields.DecimalField(max_digits=5, decimal_places=2)
    caution = models.fields.DecimalField(max_digits=5, decimal_places=2)
    tag = models.fields.CharField(choices=Tag.choices, max_length=5)
    date_creation = models.fields.DateField(auto_now_add=True)

    proprietaire = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)


class Abonnement(models.Model):

    date_achat = models.fields.DateField(auto_now_add=True)
    date_debut = models.fields.DateField(null=True, blank=True)
    date_fin = models.fields.DateField(null=True, blank=True)
    
    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)


class Avis(models.Model):

    date_creation = models.fields.DateField(auto_now_add=True)
    commentaire = models.fields.CharField(max_length=200, null=True, blank=True)
    note = models.fields.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    auteur = models.ForeignKey(Utilisateur, null=True, related_name='auteur_avis', on_delete=models.CASCADE)
    cible = models.ForeignKey(Utilisateur, null=True, related_name='cible_avis', on_delete=models.CASCADE)


class Location(models.Model):

    date_debut = models.fields.DateField(validators=[MinValueValidator(date.today()-timedelta(days=100)), MaxValueValidator(date.today()+timedelta(days=100))])
    date_fin = models.fields.DateField(validators=[MinValueValidator(date.today()-timedelta(days=100)), MaxValueValidator(date.today()+timedelta(days=100))])
    date_fin_reelle = models.fields.DateField(null=True, blank=True)
    valide = models.fields.BooleanField(default=False)
    payee = models.fields.BooleanField(default=False)

    objet = models.ForeignKey(Objet, null=True, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)


class Signalement(models.Model):

    class Type_signalement(models.TextChoices):
        DEFECTUEUX = 'D'
        VULGARITE = 'V'
        RETARD = 'R'
        PAIEMENT = 'P'
    
    date_creation = models.fields.DateField(auto_now_add=True)
    type_signalement = models.fields.CharField(choices=Type_signalement.choices, max_length=5)
    commentaire = models.fields.CharField(max_length=200, null=True, blank=True)
    
    auteur = models.ForeignKey(Utilisateur, null=True, related_name='auteur_signalement', on_delete=models.CASCADE)
    cible = models.ForeignKey(Utilisateur, null=True, related_name='cible_signalement', on_delete=models.CASCADE)
