from django.shortcuts import render, HttpResponseRedirect
from .forms import AbsCoursForm
from . import models




def index(request):
    aList = list(models.AbsCours.objects.all())
    return render(request, "Absences/abscours_all.html", {"ListeA": aList})

def ajout(request):
    if request.method == "POST":
        form = AbsCoursForm(request)
        if form.is_valid(): # validation du formulaire.
            abscours = form.save() # sauvegarde dans la base
            return render(request,"Absences/abscours_affiche.html", {"form": form})
        else:
            return render(request,"Absences/abscours_ajout.html",{"form": form})
    else:
        form = AbsCoursForm() # création d'un formulaire vide
        return render(request,"Absences/abscours_ajout.html",{"form" : form})

def traitement(request):
    abform = AbsCoursForm(request.POST)
    if abform.is_valid():
        abscours = abform.save()
        return HttpResponseRedirect("/Absences/abscours_all")
    else:
        return render(request,"Absences/abscours_ajout.html",{"form" : abform})

def affiche(request, id):
    abscours=models.AbsCours.objects.get(pk=id)
    return render(request, "Absences/abscours_affiche.html", {"AbsCours":abscours})

def update(request, id):
    abcours=models.AbsCours.objects.get(pk=id)
    abform = AbsCoursForm(abcours.dico())
    return render(request, 'Absences/abscours_update.html', {"form":abform, "id":id})

def delete(request, id):
    abcours = models.AbsCours.objects.get(pk=id)
    abcours.delete()
    return HttpResponseRedirect("/Absences/abscours_all")

def traitementupdate(request, id):
    abform=AbsCoursForm(request.POST)
    if abform.is_valid():
        abcours = abform.save(commit=False)
        abcours.id=id;
        abcours.save()
        return HttpResponseRedirect('/Absences/abscours_all')
    else:
        return render(request, "Absences/abscours_update.html", {"form":abform, "id":id})