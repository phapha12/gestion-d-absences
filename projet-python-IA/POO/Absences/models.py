from django.db import models

# Create your models here.
class Groupes(models.Model):
    nomgroupe = models.CharField(max_length=100) #eeeeeeesqfsfs

    def __str__(self):
        chaine = f" Groupe : '{self.nomgroupe}'"
        return chaine

    def dico(self):
        return {"nomgroupe": self.nomgroupe}


class Etudiants(models.Model):
    nometu = models.CharField(max_length=100)
    prenometu = models.CharField(max_length=100)
    emailetu = models.CharField(max_length=50)
    photoetu = models.ImageField(null=True, blank=True, upload_to='images/')
    groupesetu = models.ForeignKey("groupes", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.nometu} {self.prenometu}, Groupe : {self.groupesetu.nomgroupe} | E-MAIL :  {self.emailetu} Photo : {self.photoetu}"
        return chaine

    def dico(self):
        return {"nometu": self.nometu, "prenometu": self.prenometu,"emailetu": self.emailetu, "photoetu": self.photoetu, "groupesetu":self.groupesetu}

class Enseignant(models.Model):
    nomens = models.CharField(max_length = 100)
    prenomens = models.CharField(max_length = 100)
    emailens = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"Monsieur {self.nomens} {self.prenomens} | E-MAIL : {self.emailens}"
        return chaine

    def dico(self):
        return {"nomens": self.nomens, "prenomens": self.prenomens,"emailens": self.emailens}


class Cours(models.Model):
    titre_du_cours = models.CharField(max_length = 100)
    date = models.DateField(blank=True, null = True)
    enseignant = models.ForeignKey("enseignant", on_delete=models.CASCADE, default=None)
    duree = models.CharField(max_length = 10)
    groupe = models.ForeignKey("groupes", on_delete=models.CASCADE, default=None)


    def __str__(self):
        chaine = f"Cours de {self.titre_du_cours}, le {self.date}. Enseignant : M.{self.enseignant.nomens} | durée : {self.duree}, Groupe : {self.groupe}"
        return chaine

    def dico(self):
        return {"titre_du_cours": self.titre_du_cours, "date": self.date,"enseignant": self.enseignant, "duree": self.duree, "groupe": self.groupe}

class AbsCours(models.Model):
    cours = models.ForeignKey("cours", on_delete=models.CASCADE, default=None)
    etudiants = models.ManyToManyField(Etudiants, blank=False)
    justified = models.BooleanField()
    justificatif = models.TextField(null = True, blank=True)


    def __str__(self):
        chaine = f"Absences au cours de {self.cours.titre_du_cours} de M.{self.cours.enseignant.nomens} {self.cours.enseignant.prenomens}"

        return chaine

    def dico(self):
        return {"cours": self.cours, "etudiants": self.etudiants,"justified": self.justified, "justificatif": self.justificatif}