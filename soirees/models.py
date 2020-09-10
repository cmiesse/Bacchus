from django.db import models

class Soiree(models.Model):
    nom = models.CharField(max_length=255)
    date = models.DateField()
