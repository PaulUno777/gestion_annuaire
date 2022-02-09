from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    isAdmin = models.BooleanField(null=False)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateInscription = models.DateField(auto_now_add=True)

class Tag(models.Model):
    valeur = models.CharField(max_length=20,unique=True)

class Etablissement(models.Model):
    nom = models.CharField(max_length=100)
    localite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    webUrl = models.CharField(max_length=100,null=True)
    rue = models.CharField(max_length=100)
    codePostal = models.CharField(max_length=20)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    image = models.ImageField()

class Bar(Etablissement):
    fumeur = models.BooleanField(null=True)
    restauration = models.BooleanField(null=True)

class Hotel(Etablissement):
    etoiles = models.IntegerField()
    prixChambre = models.IntegerField(null=False)


class Tagger(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    etablissement = models.ForeignKey(Etablissement,null=False,on_delete=models.CASCADE)
    Tag = models.ForeignKey(User,null=False,on_delete=models.CASCADE)

class Commentaire(models.Model):
    score = models.IntegerField(null=True)
    text = models.CharField(max_length=500,null=False)
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    etablissement = models.ForeignKey(Etablissement,null=False,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True,null=False)

class JourFermeture(models.Model):
    jour_possible = (('lundi','lundi'),('mardi','mardi'),('mercredi','mercredi'),('jeudi','jeudi'),('vendredi','vendredi'),('samedi','samedi'))
    jour = models.CharField(choices=jour_possible,max_length=10,null=False)
    heure = models.CharField(choices=(('AM','AM'),('PM','PM')),max_length=2)

class Restaurant(Etablissement):
    platPrix = models.IntegerField()
    places = models.IntegerField()
    platEmporte = models.BooleanField()
    livraison = models.BooleanField()
    jourFermeture = models.ManyToManyField(JourFermeture)