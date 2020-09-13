from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_post = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Soiree(models.Model):
    theme = models.CharField(max_length=100)
    date_soiree =models.DateField()

class Vin(models.Model):
    pays= models.CharField(max_length=100)
    region= models.CharField(max_length=100)
    appelation= models.CharField(max_length=100)
    cru= models.CharField(max_length=100)
    BLANC='blanc'
    ROSE='rosé'
    ROUGE='rouge'
    COULEUR_CHOICES = [
        (BLANC,'Blanc'),
        (ROSE, 'Rosé'),
        (ROUGE, 'Rouge'),
    ]
    couleur= models.CharField(max_length=5, choices=COULEUR_CHOICES, default=ROUGE)
    lieu_achat= models.CharField(max_length=100)
    prix_achat= models.FloatField()
    millesime=models.IntegerField()
    cepages= models.CharField(max_length=100)
    proprietaire= models.CharField(max_length=100)
    degre= models.FloatField()

    def get_absolute_url(self):
        return reverse('vin-detail', kwargs={'pk': self.pk})