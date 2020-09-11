from django.db import models

class Fiche(models.Model):
    limpidite = models.CharField(max_length=11)
    intensite_couleurs = models.CharField(max_length=8)
    robe_blanc = models.CharField(max_length=15)
    robe_rose = models.CharField(max_length=15)
    robe_rouge = models.CharField(max_length=15)
    viscosite = models.CharField(max_length=15)
