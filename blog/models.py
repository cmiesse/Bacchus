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

    def __str__(self):
        return self.appelation

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
        ('teinté de vert','Teinté de vert'),
        ('jaune pâle','Jaune pâle'),
        ('jaune', 'Jaune'),
        ('paille','Paille'),
        ('or','Or'),
        ('doré','Doré'),
        ('ambré','Ambré'),
        ('madérisé','Madérisé')
    ]
    robe_blanc = models.CharField(max_length=20, choices=ROBE_BLANC, blank=True, null=True)
    ROBE_ROSE = [
        ('gris','Gris'),
        ('rosé','Rosé'),
        ('rosé framboise','Rosé framboise'),
        ('rosé orange','Rosé orange')
    ]
    robe_rose = models.CharField(max_length=20, choices=ROBE_ROSE, blank=True, null=True)
    ROBE_ROUGE = [
        ('violet pourpre','Violet pourpre'),
        ('grenat','Grenat'),
        ('rubis','Rubis'),
        ('incarnat','Incarnat'),
        ('carmin','Carmin'),
        ('vermillon','Vermillon'),
        ('brique','Brique'),
        ('tuile','Tuile'),
        ('orange','Orange')
    ]
    robe_rouge = models.CharField(max_length=20, choices=ROBE_ROUGE, blank=True, null=True)
    VISCOSITE = [
        ('léger','Léger'),
        ('normal','Normal'),
        ('lourd','Lourd'),
        ('gras','Gras')
    ]
    viscosite = models.CharField(max_length=20, choices=VISCOSITE)
    commentaires_visuel = models.CharField(max_length=255)
    INTENSITE_NEZ = [
        ('défectueux','Défectueux'),
        ('faible','Faible'),
        ('modéré','Modéré'),
        ('marqué','Marqué'),
        ('puissant','Puissant')
    ]
    intensite_nez = models.CharField(max_length=20, choices=INTENSITE_NEZ)
    RAPPEL = [
        ('nul','Nul'),
        ('léger','Léger'),
        ('moyen','Moyen'),
        ('distinct','Distinct'),
        ('prononcé','Prononcé')
    ]
    rappel_fruit = models.CharField(max_length=20, choices=RAPPEL)
    rappel_floral = models.CharField(max_length=20, choices=RAPPEL)
    rappel_epice = models.CharField(max_length=20, choices=RAPPEL)
    BOUQUET = [
        ('ordinaire','Ordinaire'),
        ('agréable','Agréable'),
        ('fin','Fin'),
        ('complexe','Complexe'),
        ('expressif','Expresssif')
    ] 
    bouquet = models.CharField(max_length=20, choices=BOUQUET)
    commentaires_arome = models.CharField(max_length=255)
    DOUCEUR = [
        ('extra-sec','Extra-sec'),
        ('sec','Sec'),
        ('demi-sec','Demi-sec'),
        ('moelleux','Moelleux'),
        ('liquoreux','Liquoreux')
    ]
    douceur = models.CharField(max_length=20, choices=DOUCEUR, blank=True, null=True)
    TANINS = [
        ('maigre','Maigre'),
        ('fondu','Fondu'),
        ('savoureux','Savoureux'),
        ('présent','Présent'),
        ('astringent','Astringent'),
        ('rude','Rude')
    ]
    tanins = models.CharField(max_length=20, choices=TANINS, blank=True, null=True)
    ACIDITE = [
        ('plat','Plat'),
        ('mou','Mou'),
        ('souple','Souple'),
        ('frais','Frais'),
        ('vif','Vif'),
        ('acide','Acide'),
        ('vert','Vert')
    ]
    acidite = models.CharField(max_length=20, choices=ACIDITE)
    CORPS = [
        ('mince','Mince'),
        ('plaisant','Plaisant'),
        ('rond','Rond'),
        ('ferme','Ferme'),
        ('ample','Ample'),
        ('charnu','Charnu'),
        ('étoffé','Etoffé')
    ]
    corps = models.CharField(max_length=20,choices=CORPS)
    PERSISTANCE = [
        ('courte','Courte'),
        ('moyenne','Moyenne'),
        ('longue','Longue'),
        ('prolongée','Prolongée')
    ]
    persistance = models.CharField(max_length=20, choices=PERSISTANCE)
    EQUILIBRE = [
        ('déséquilibré','Déséquilibré'),
        ('fragile','Fragile'),
        ('correct','Correct'),
        ('bien','Bien'),
        ('très bien','Très bien'),
        ('parfait','Parfait')
    ]
    equilibre = models.CharField(max_length=20, choices=EQUILIBRE)
    commentaires_saveur = models.CharField(max_length=255)
    STADE_MATURATION = [
        ('passé','Passé'),
        ('vieilli','Vieilli'),
        ('épanoui','Epanoui'),
        ("s'ouvre", "S'ouvre"),
        ('fermé','Fermé')
    ]
    stade_maturation = models.CharField(max_length=20,choices=STADE_MATURATION)
    IMPRESSION_TECHNIQUE = [
        ('médiocre','Médiocre'),
        ('acceptable','Acceptable'),
        ('correct','Correct'),
        ('bon','Bon'),
        ('très bon', 'Très bon'),
        ('remarquable','Remarquable')
    ]
    impression_technique = models.CharField(max_length=20,choices=IMPRESSION_TECHNIQUE)
    commentaires_ensemble = models.CharField(max_length=255)
    IMPRESSION_PERSONNELLE=[
        ('quelconque','Quelconque'),
        ('satisfaisant','Satisfaisant'),
        ('bien','Bien'),
        ('très bien','Très bien')
    ]
    impression_personnelle = models.CharField(max_length=20, choices=IMPRESSION_PERSONNELLE)
    date_degustation = models.DateField(default=timezone.now)
    periode_garde = models.CharField(max_length=20)
    vin = models.ForeignKey(Vin, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('fiche-detail', kwargs={'pk': self.pk})
