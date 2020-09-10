from django.db import models

class Vin(models.Model):
    appelation = models.CharField(max_length=50)
    cru = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    region = models.CharField(max_length=50, null=True, blank=True)
    lieuAchat = models.CharField(max_length=50, null=True, blank=True)
    prix = models.FloatField()
    millesime = models.IntegerField()
    cepage = models.CharField(max_length=100)
    proprietaire = models.CharField(max_length=50, null=True, blank=True)
    degre = models.FloatField()
