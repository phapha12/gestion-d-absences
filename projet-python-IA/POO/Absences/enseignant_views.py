from django.shortcuts import render, HttpResponseRedirect
from .forms import EnseignantForm
from . import models




def index(request):
    eList = list(models.Enseignant.objects.all())
    return render(request, "Absences/enseignant_all.html", {"ListeE": eList})

def ajout(request):
    if request.method == "POST":
        form = EnseignantForm(request)
        if form.is_valid(): # validation du formulaire.
            enseignant = form.save() # sauvegarde dans la base
            return render(request,"Absences/enseignant_affiche.html", {"form": form}) #aa
        else:
            return render(request,"Absences/enseignant_ajout.html",{"form": form})
    else:
        form = EnseignantForm() # création d'un formulaire vide
        return render(request,"Absences/enseignant_ajout.html",{"form" : form})


        

def traitement(request):
    eform = EnseignantForm(request.POST)
    if eform.is_valid():
        enseignant = eform.save()
        return HttpResponseRedirect("/Absences/enseignant_all")
    else:
        return render(request,"Absences/enseignant_ajout.html",{"form" : eform})

def affiche(request, id):
    enseignant=models.Enseignant.objects.get(pk=id)
    return render(request, "Absences/enseignant_affiche.html", {"Enseignant":enseignant})

def update(request, id):
    enseignant=models.Enseignant.objects.get(pk=id)
    eform = EnseignantForm(enseignant.dico())
    return render(request, 'Absences/enseignant_update.html', {"form":eform, "id":id})

def delete(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    enseignant.delete()
    return HttpResponseRedirect("/Absences/enseignant_all")

def traitementupdate(request, id):
    eform=EnseignantForm(request.POST)
    if eform.is_valid():
        enseignant = eform.save(commit=False)
        enseignant.id=id;
        enseignant.save()
        return HttpResponseRedirect('/Absences/enseignant_all')
    else:
        return render(request, "Absences/enseignant_update.html", {"form":eform, "id":id})
