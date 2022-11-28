from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class GroupesForm(ModelForm):
    class Meta:
        model = models.Groupes
        fields = ('nomgroupe',)
        labels = {
            'nomgroupe': _('Nom du groupe')
        }

class EtudiantsForm(ModelForm):
    class Meta:
        model = models.Etudiants
        fields=('nometu', 'prenometu', 'emailetu', 'photoetu', 'groupesetu')
        labels = {
            'nometu' : _("Nom de l'étudiant"),
            'prenometu' : _('Prénom de l\'étudiant'),
            'emailetu' : _('Email de l\'étudiant'),
            'photoetu' : _('Photo de l\'étudiant'),
            'groupesetu' : _('Groupes de l\'étudiant'),
        }

class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('nomens', 'prenomens', 'emailens')
        labels = {
            'nomens' : _('Nom enseignant') ,
            'prenomens' : _('Prénom enseignant'),
            'emailens' : _('e-mail enseignant')
        }

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = ('titre_du_cours', 'date', 'enseignant', 'duree', 'groupe')
        labels = {
            'titre_du_cours' : _('Titre du cours') ,
            'date' : _('Date du cours'),
            'enseignant' : _('Enseignant du cours'),
            'duree' : _('Durée du cours'),
            'groupe' : _('Groupe'),
        }

class AbsCoursForm(ModelForm):
    class Meta:
        model = models.AbsCours
        fields = ('cours', 'etudiants', 'justified', 'justificatif',)
        labels = {
            'cours' : _('Cours') ,
            'Etudiants' : _('Etudiants absents'),
            'justified' : _('Justifié'),
            'justificatif' : _('Justificatif'),
        }
