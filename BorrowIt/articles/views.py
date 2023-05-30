from django.shortcuts import render
from django.shortcuts import redirect

from datetime import timedelta, date

from articles.models import Objet, Utilisateur, Abonnement, Avis, Location, Signalement
from articles.forms import ObjetForm, UtilisateurForm, AvisForm, LocationForm, SignalementForm


###### CREATE ######

def inscription(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            return object_list(request, id=utilisateur.id)
    else:
        form = UtilisateurForm()
    return render(request, 'articles/forms/inscription.html', {'id':-1, 'form':form})


def connexion(request):
    if request.method == 'GET':
        mail = request.GET.get('mail')
        mot_de_passe = request.GET.get('mot_de_passe')
        print(mail, mot_de_passe)
        if mail is not None and mot_de_passe is not None:
            user = Utilisateur.objects.filter(mail=mail, mot_de_passe=mot_de_passe)
            if user.exists():
                return object_list(request, id = user[0].id)
    return render(request, 'articles/forms/connexion.html', {'id':-1})


def add_objet(request, id):
    if request.method == 'POST':
        form = ObjetForm(request.POST)
        if form.is_valid():
            objet = form.save()
            objet.proprietaire = Utilisateur.objects.get(id=id)
            objet.save()
            return object_list(request, id=objet.proprietaire.id)
    else:
        form = ObjetForm()
    return render(request, 'articles/forms/add_objet.html', {'id':id, 'form':form})


def abonnements(request, id):
    client = Utilisateur.objects.get(id=id)
    abonnements = Abonnement.objects.filter(client=client)
    fin_abonnements = None
    abonnement_actif = False
    if abonnements.exists():
        fin_abonnements = max([abo.date_fin for abo in abonnements])
        if fin_abonnements >= date.today():
            abonnement_actif = True
        
    if request.method == "POST":
        new_abonnement = Abonnement()
        new_abonnement.client = client
        if not abonnements.exists():
            fin_abonnements = date.today()-timedelta(1)
        fin_abonnements = max(fin_abonnements, date.today())
        new_abonnement.date_debut = fin_abonnements+timedelta(1)
        new_abonnement.date_fin = fin_abonnements+timedelta(30)
        new_abonnement.save()
    return render(request, 'articles/abonnements.html', {'id':id, 'fin_abonnements':fin_abonnements, 'abonnement_actif':abonnement_actif})


def add_avis(request, id_user, id_cible):
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            avis = form.save()
            avis.auteur = Utilisateur.objects.get(id=id_user)
            avis.cible = Utilisateur.objects.get(id=id_cible)
            avis.save()
            return see_profile(request, id_user, id_cible)
    else:
        form = AvisForm()
    return render(request, 'articles/forms/add_avis.html', {'form':form, 'id':id_user})


def add_signalement(request, id_user, id_cible):
    if request.method == 'POST':
        form = SignalementForm(request.POST)
        if form.is_valid():
            signalement = form.save()
            signalement.auteur = Utilisateur.objects.get(id=id_user)
            signalement.cible = Utilisateur.objects.get(id=id_cible)
            signalement.save()
            return see_profile(request, id_user, id_cible)
    else:
        form = SignalementForm()
    return render(request, 'articles/forms/add_signalement.html', {'form':form, 'id':id_user})


###### READ ######

def object_list(request, id = -1, tag = ""):
    print(156461354613, id, tag)
    user_connected = Utilisateur.objects.filter(id=id)
    if user_connected.exists():
        user_connected = user_connected[0]
    else:
        user_connected = None
    objects = Objet.objects.exclude(proprietaire=user_connected)

    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if keyword is not None:
            objects = Objet.objects.filter(nom__icontains=keyword).exclude(proprietaire=user_connected)
        
    dict_tag = {
            'Outils':('O', "https://i.goopics.net/k9x1py.png"),
            'Films':('F', "https://i.goopics.net/p9ujew.png"),
            'Livres':('L', "https://i.goopics.net/y7bhsj.png"),
            'Jeux':('J', "https://i.goopics.net/oazyxx.png"), 
            'Informatique':('IF', "https://i.goopics.net/2ij49a.png"), 
            'Véhicules':('V', "https://i.goopics.net/6wbehu.png"), 
            'Mode':('MO', "https://i.goopics.net/8tds6u.png"), 
            'Immobilier':('IM', "https://i.goopics.net/6uc1yi.png"), 
            'Musique':('MU', "https://i.goopics.net/9himml.png"), 
            'Autres':('A', "https://i.goopics.net/727i75.png")
        }
        
    if tag != "":
        objects = Objet.objects.filter(tag=dict_tag[tag][0]).exclude(proprietaire=user_connected)
    
    return render(request, 'articles/home.html', {'objects':objects, 'id':id, 'dict_tag':dict_tag})


def see_profile(request, id_connected = -1, id_target = -1):
    print(1631316536851)
    if id_connected == -1:
        connected = False
        my_profile = False
        target = Utilisateur.objects.get(id=id_target)
        fin_abonnement_actuel = None
    elif id_target == -1:
        connected = True
        my_profile = True
        target = Utilisateur.objects.get(id=id_connected)
        abonnements = Abonnement.objects.filter(client=target)
        if abonnements.exists():
            fin_abonnement_actuel = max([abo.date_fin for abo in abonnements])
        else:
            fin_abonnement_actuel = None
    else:
        connected = True
        my_profile = False
        target = Utilisateur.objects.get(id=id_target)
        fin_abonnement_actuel = None
    objects = Objet.objects.filter(proprietaire=target)

    print(id_connected, connected, my_profile, target, fin_abonnement_actuel)

    return render(request, 'articles/profile.html', {'id':id_connected, 'connected':connected, 'my_profile':my_profile, 'target':target, 'fin_abonnement_actuel':fin_abonnement_actuel, 'objects':objects})


def see_object(request, id_object, id_connected = -1):
    objet = Objet.objects.get(id=id_object)

    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            location.emprunteur = Utilisateur.objects.get(id=id_connected)
            location.objet = objet
            location.save()
            return object_list(request, id = id_connected)
    
    form = LocationForm()
    return render(request, 'articles/objet.html', {'id':id_connected, 'objet':objet, 'form':form})


def emprunts(request, id, location_list_to_show='attente_validation'):
    print(location_list_to_show)
    user = Utilisateur.objects.get(id=id)
    match location_list_to_show:
        case 'attente_validation':
            locations = Location.objects.filter(emprunteur=user, valide=False)
        case 'validees':
            locations = Location.objects.filter(emprunteur=user, valide=True, date_debut__gt=date.today())
        case 'en_cours':
            locations = Location.objects.filter(emprunteur=user, valide=True, payee=True, date_debut__lte=date.today(), date_fin_reelle__isnull=True)
        case 'passees':
            locations = Location.objects.filter(emprunteur=user, date_fin_reelle__isnull=False)

    context = {
        'id': id,
        'location_list_to_show': location_list_to_show,
        'locations': locations
    }
    return render(request, 'articles/emprunts.html', context)


def location_list(request, id, location_list_to_show='attente_validation'):
    print(location_list_to_show)
    user = Utilisateur.objects.get(id=id)
    match location_list_to_show:
        case 'attente_validation':
            locations = Location.objects.filter(emprunteur=user, valide=False)
        case 'validees':
            locations = Location.objects.filter(emprunteur=user, valide=True, date_debut__gt=date.today())
        case 'en_cours':
            locations = Location.objects.filter(emprunteur=user, valide=True, payee=True, date_debut__lte=date.today(), date_fin_reelle__isnull=True)
        case 'passees':
            locations = Location.objects.filter(emprunteur=user, date_fin_reelle__isnull=False)

    context = {
        'id': id,
        'location_list_to_show': location_list_to_show,
        'locations': locations
    }
    return render(request, 'articles/locations.html', context)


###### UPDATE ######

def modifier_profil(request, id):
    utilisateur = Utilisateur.objects.get(id=id)
    if request.method == 'POST':
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('profil', utilisateur.id)
    else:
        form = UtilisateurForm(instance=utilisateur)
    return render(request, 'articles/forms/profile_update.html', {'id':id, 'form':form})


def valider_location(request, id, id_location):
    location = Location.objects.get(id=id_location)
    location.valide = True
    location.save()
    return location_list(request, id)


def terminer_location(request, id, id_location, date_fin_reelle=date.today()):
    location = Location.objects.get(id=id_location)
    location.date_fin_reelle = date_fin_reelle
    location.save()
    return location_list(request, id)


def payer_location(request, id, id_location):
    location = Location.objects.get(id=id_location)
    location.payee = True
    location.save()
    return emprunts(request, id, location_list_to_show="attente_paiement")


###### DELETE ######


def delete_emprunt(request, id, id_location):
    location = Location.objects.get(id=id_location)
    if request.method == 'POST':
        location.delete()
        return emprunts(request, id)
    return emprunts(request, id)


def delete_location(request, id_user, id_location):
    location = Location.objects.get(id=id_location)
    if request.method == 'POST':
        location.delete()
        return redirect('reception-demandes', id_user)
    return render(request, 'articles/location_delete.html', {'location': location})
