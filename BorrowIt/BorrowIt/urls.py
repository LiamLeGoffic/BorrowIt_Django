"""
URL configuration for BorrowIt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    ###### CREATE ######
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('<int:id>/nouvel-objet/', views.add_objet, name='add-objet'),
    path('<int:id>/abonnements/', views.abonnements, name='abonnements'),
    path('<int:id_user>/<int:id_cible>/nouvel-avis/', views.add_avis, name='add-avis'),
    path('<int:id_user>/<int:id_cible>/nouveau-signalement/', views.add_signalement, name='add-signalement'),
    ###### READ ######
    path('', views.object_list, name='home'),
    path('<int:id>/', views.object_list, name='home-connected'),
    path('<str:tag>/', views.object_list, name='search-by-tag-unconnected'),
    path('<int:id>/search-by-tag/<str:tag>/', views.object_list, name='search-by-tag-connected'),
    path('<int:id_connected>/mon-profil/', views.see_profile, name='my-profile'),
    path('profil/<int:id_target>/', views.see_profile, name='profil-target-unconnected'),
    path('<int:id_connected>/profil/<int:id_target>/', views.see_profile, name='profil-target-connected'),
    path('objet/<int:id_object>/', views.see_object, name='objet-unconnected'),
    path('<int:id_connected>/objet/<int:id_object>/', views.see_object, name='objet-connected'),
    path('<int:id>/emprunts/', views.emprunts, name='emprunts'),
    path('<int:id>/emprunts/<str:location_list_to_show>/', views.emprunts, name='emprunts-loc-list'),
    path('<int:id>/locations/', views.location_list, name='location-list'),
    path('<int:id>/locations/<str:location_list_to_show>/', views.location_list, name='location-list-panel'),
    ###### UPDATE ######
    path('<int:id>/profil/modifier-profil/', views.modifier_profil, name='modifier-profil'),
    path('<int:id>/emprunts/<int:id_location>/payer/', views.payer_location, name='payer-loc'),
    path('<int:id>/locations/<int:id_location>/valider/', views.valider_location, name='valider-loc'),
    path('<int:id>/locations/<int:id_location>/terminer/', views.terminer_location, name='terminer-loc'),
    ###### DELETE ######
    path('<int:id>/emprunts/<int:id_location>/supprimer-emprunt/', views.delete_emprunt, name='delete-emprunt'),
    path('<int:id>/locations/<int:id_location>/supprimer-location/', views.delete_location, name='delete-location'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
