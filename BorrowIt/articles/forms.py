from django import forms
from articles.models import Objet, Utilisateur, Avis, Location, Signalement


class ObjetForm(forms.ModelForm):
    class Meta:
        model = Objet
        exclude = ('date_creation', 'proprietaire')


class UtilisateurForm(forms.ModelForm):
   class Meta:
        model = Utilisateur
        exclude = ('date_creation',)
        

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        exclude = ('date_creation', 'auteur', 'cible',)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ('date_fin_reelle', 'valide', 'payee', 'objet', 'emprunteur',)


class SignalementForm(forms.ModelForm):
    class Meta:
        model = Signalement
        exclude = ('date_creation', 'auteur', 'cible',)
