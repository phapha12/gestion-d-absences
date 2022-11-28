from django.shortcuts import render
from . forms import EtudiantsForm
from . import models
from django.http import HttpResponseRedirect
# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = EtudiantsForm(request)
        if form.is_valid():
            etudiants = form.save()
            return render(request,"Absences/etudiants_all/affiche.html",{"Etudiants" : etudiants})
        else:
            return render(request,"Absences/etudiants_ajout.html",{"form": form})
    else:
        form = EtudiantsForm()
        return render(request,"Absences/etudiants_ajout.html",{"form" : form})

def traitement(request):
    etform = EtudiantsForm(request.POST)
    if etform.is_valid():
        etudiants=etform.save()
        return HttpResponseRedirect("/Absences/etudiants_all")
    else:
        return render(request, 'Absences/etudiants_ajout.html', {'form':etform})

def index(request):
    etList = list(models.Etudiants.objects.all())
    return render(request, "Absences/etudiants_all.html", {"Liste": etList})

def affiche(request, id):
    etudiants=models.Etudiants.objects.get(pk=id)
    return render(request, "Absences/etudiants_affiche.html", {"Etudiants":etudiants})

def update(request, id):
    etudiants=models.Etudiants.objects.get(pk=id)
    etform = EtudiantsForm(etudiants.dico())
    return render(request, 'Absences/etudiants_update.html', {"form":etform, "id":id})

def delete(request, id):
    etudiants = models.Etudiants.objects.get(pk=id)
    etudiants.delete()
    return HttpResponseRedirect("/Absences/etudiants_all")

def traitementupdate(request, id):
    etform=EtudiantsForm(request.POST)
    if etform.is_valid():
        etudiants = etform.save(commit=False)
        etudiants.id=id;
        etudiants.save()
        return HttpResponseRedirect('/Absences/etudiants_all')
    else:
        return render(request, "Absences/etudiants_update.html", {"form":etform, "id":id})