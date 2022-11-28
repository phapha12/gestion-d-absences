from django.shortcuts import render, HttpResponseRedirect
from .forms import CoursForm
from . import models




def index(request):
    cList = list(models.Cours.objects.all())
    return render(request, "Absences/cours_all.html", {"ListeC": cList})

def ajout(request):
    if request.method == "POST":
        form = CoursForm(request)
        if form.is_valid():
            cours = form.save()
            return render(request,"Absences/cours_affiche.html", {"form": form})
        else:
            return render(request,"Absences/cours_ajout.html",{"form": form})
    else:
        form = CoursForm()
        return render(request,"Absences/cours_ajout.html",{"form" : form})

def traitement(request):
    cform = CoursForm(request.POST)
    if cform.is_valid():
        cours = cform.save()
        return HttpResponseRedirect("/Absences/cours_all")
    else:
        return render(request,"Absences/cours_ajout.html",{"form" : cform})

def affiche(request, id):
    cours=models.Cours.objects.get(pk=id)
    return render(request, "Absences/cours_affiche.html", {"Cours":cours})

def update(request, id):
    cours=models.Cours.objects.get(pk=id)
    cform = CoursForm(cours.dico())
    return render(request, 'Absences/cours_update.html', {"form":cform, "id":id})

def delete(request, id):
    cours = models.Cours.objects.get(pk=id)
    cours.delete()
    return HttpResponseRedirect("/Absences/cours_all")

def traitementupdate(request, id):
    cform=CoursForm(request.POST)
    if cform.is_valid():
        cours = cform.save(commit=False)
        cours.id=id;
        cours.save()
        return HttpResponseRedirect('/Absences/cours_all')
    else:
        return render(request, "Absences/cours_update.html", {"form":eform, "id":id})