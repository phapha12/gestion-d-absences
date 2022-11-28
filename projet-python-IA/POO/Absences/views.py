from django.shortcuts import render
from . forms import GroupesForm
from . import models
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponseRedirect("/Login.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="Absences/register.html", context={"register_form":form})
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return HttpResponseRedirect("/Absences/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="Absences/login.html", context={"login_form":form})
def ajout(request):
    if request.method == "POST":
        form = GroupesForm(request)
        if form.is_valid():
            groupe = form.save()
            return render(request,"Absences/affiche.html",{"Groupe" : groupe})
        else:
            return render(request,"Absences/ajout.html",{"form": form})
    else:
        form = GroupesForm()
        return render(request,"Absences/ajout.html",{"form" : form})

def traitement(request):
    gform = GroupesForm(request.POST)
    if gform.is_valid():
        groupe=gform.save()
        return HttpResponseRedirect("/Absences/")
    else:
        return render(request, 'Absences/ajout.html', {'form':gform})

def index(request):
    gList = list(models.Groupes.objects.all())
    return render(request, "Absences/index.html", {"Liste": gList})

def affiche(request, id):
    groupe=models.Groupes.objects.get(pk=id)
    return render(request, "Absences/affiche.html", {"Groupe":groupe})

def update(request, id):
    groupe=models.Groupes.objects.get(pk=id)
    gform = GroupesForm(groupe.dico())
    return render(request, 'Absences/update.html', {"form":gform, "id":id})

def delete(request, id):
    groupe = models.Groupes.objects.get(pk=id)
    groupe.delete()
    return HttpResponseRedirect("/Absences/")

def traitementupdate(request, id):
    gform=GroupesForm(request.POST)
    if gform.is_valid():
        groupe = gform.save(commit=False)
        groupe.id=id;
        groupe.save()
        return HttpResponseRedirect('/Absences/')
    else:
        return render(request, "Absences/update.html", {"form":gform, "id":id})
