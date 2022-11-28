from django.urls import path

from . import views, etudiants_views, enseignant_views, cours_views, abscours_views
app_name = 'Absences'
urlpatterns = [
    #register
    path("register", views.register_request, name="register"),
    #login
    path("login", views.login_request, name="login"),
    #Groupe
    path('', views.index),
    path('ajout/', views.ajout),
    path('delete/<int:id>', views.delete),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>', views.traitementupdate),
    #Enseignant
    path('enseignant_all/ajout/', enseignant_views.ajout),
    path('enseignant_all/delete/<int:id>', enseignant_views.delete),
    path('enseignant_traitement/', enseignant_views.traitement),
    path('enseignant_all/affiche/<int:id>/', enseignant_views.affiche),
    path('enseignant_all/update/<int:id>/', enseignant_views.update),
    path('enseignant_traitementupdate/<int:id>', enseignant_views.traitementupdate),
    path('enseignant_all/', enseignant_views.index),
    #Cours
    path('cours_all/ajout/', cours_views.ajout),
    path('cours_all/delete/<int:id>', cours_views.delete),
    path('cours_traitement/', cours_views.traitement),
    path('cours_all/affiche/<int:id>/', cours_views.affiche),
    path('cours_all/update/<int:id>/', cours_views.update),
    path('cours_traitementupdate/<int:id>', cours_views.traitementupdate),
    path('cours_all/', cours_views.index),
    #Etudiants
    path('etudiants_all/ajout/', etudiants_views.ajout),
    path('etudiants_all/delete/<int:id>/', etudiants_views.delete),
    path('etudiants_traitement/', etudiants_views.traitement),
    path('etudiants_all/affiche/<int:id>/', etudiants_views.affiche),
    path('etudiants_all/update/<int:id>/', etudiants_views.update),
    path('etudiants_traitementupdate/<int:id>', etudiants_views.traitementupdate),
    path('etudiants_all/', etudiants_views.index),
    #Absences à des cours
    path('abscours_all/ajout/', abscours_views.ajout),
    path('abscours_all/delete/<int:id>/', abscours_views.delete),
    path('abscours_traitement/', abscours_views.traitement),
    path('abscours_all/affiche/<int:id>/', abscours_views.affiche),
    path('abscours_all/update/<int:id>/', abscours_views.update),
    path('abscours_traitementupdate/<int:id>', abscours_views.traitementupdate),
    path('abscours_all/', abscours_views.index),

]
