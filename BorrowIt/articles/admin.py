from django.contrib import admin
from articles.models import Objet, Utilisateur, Abonnement, Avis, Location, Signalement


class ObjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'url_photo', 'prix_jour', 'caution', 'date_creation')


class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'numero_tel', 'mail', 'mot_de_passe')


class AbonnementAdmin(admin.ModelAdmin):
    list_display = ('date_debut', 'date_fin', 'date_achat')

    
class AvisAdmin(admin.ModelAdmin):
    list_display = ('date_creation', 'note', 'commentaire')

    
class LocationAdmin(admin.ModelAdmin):
    list_display = ('date_debut', 'date_fin', 'valide', 'payee', 'date_fin_reelle')

    
class SignalementAdmin(admin.ModelAdmin):
    list_display = ('date_creation', 'type_signalement', 'commentaire')



admin.site.register(Objet, ObjetAdmin)
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Abonnement, AbonnementAdmin)
admin.site.register(Avis, AvisAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Signalement, SignalementAdmin)