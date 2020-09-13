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

class Fiche(models.Model):
    LIMPIDITE = [
        ('trouble','Trouble'),
        ('brillant','Brillant'),
        ('scintillant','Scintillant')
    ]
    limpidite = models.CharField(max_length=20, choices=LIMPIDITE,default='brillant')
    INTENSITE_COULEURS = [
        ('pâle','Pâle'),
        ('moyenne','Moyenne'),
        ('profonde','Profonde'),
        ('foncée','Foncée'),
        ('soutenue','Soutenue')
    ]
    intensite_couleurs = models.CharField(max_length=20, choices=INTENSITE_COULEURS,default='moyenne')
    ROBE_BLANC = [
        ('teinté de vert','Tienté de vert'),
        ('jaune pâle','Jaune pâle),
        ('jaune', 'Jaune'),
        ('paille','Paille'),
        ('or','Or'),
        ('doré','Doré'),
        ('ambré','Ambré'),
        ('madérisé','Madérisé')
    ]
    robe_blanc = models.CharField(max_length=20, choices=ROBE_BLANC)
    robe_rose = models.CharField()
    robe_rouge = models.CharField()
    viscosite = models.CharField()
    commentaires_visuel = models.CharField()
    intensite_nez = models.CharField()
    rappel_fruit = models.CharField()
    rappel_floral = models.CharField()
    rappel_epice = models.CharField() 
    bouquet = models.CharField()
    commentaires_arome = models.CharField()
    douceur = models.CharField()
    tanins = models.CharField()
    acidite = models.CharField()
    corps = models.CharField()
    persistance = models.CharField()
    equilibre = models.CharField()
    stade_maturation = models.CharField()
    impression_technique = models.CharField()
    commentaires_ensemble = models.CharField()
    impression_personnelle = models.CharField()
    date_degustation = models.DateField(default=timezone.now)
    periode_garde = models.CharField()
    vin = models.ForeignKey(Vin, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
