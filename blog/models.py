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
    theme = models.CharField(max_length=100, verbose_name= 'Thème')
    date_soiree =models.DateField(verbose_name= 'Date de la soirée')

    def get_absolute_url(self):
        return reverse('soiree-detail', kwargs={'pk': self.pk})

class Vin(models.Model):
    nom = models.CharField(max_length=100)
    pays= models.CharField(max_length=100)
    region= models.CharField(max_length=100, verbose_name= 'Région', blank=True, null=True)
    appelation= models.CharField(max_length=100, blank=True, null=True)
    cru= models.CharField(max_length=100, blank=True, null=True)
    BLANC='blanc'
    ROSE='rosé'
    ROUGE='rouge'
    COULEUR_CHOICES = [
        (BLANC,'Blanc'),
        (ROSE, 'Rosé'),
        (ROUGE, 'Rouge'),
    ]
    couleur= models.CharField(max_length=5, choices=COULEUR_CHOICES, default=ROUGE)
    lieu_achat= models.CharField(max_length=100, verbose_name= 'Lieu d\'achat', blank=True, null=True)
    prix_achat= models.FloatField(verbose_name= 'Prix d\'achat', blank=True, null=True)
    millesime=models.IntegerField(verbose_name= 'Millésime')
    cepages= models.CharField(max_length=100, verbose_name= 'Cépages', blank=True, null=True)
    proprietaire= models.CharField(max_length=100, verbose_name= 'Propriétaire', blank=True, null=True)
    degre= models.FloatField(verbose_name= 'Degré')

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('vin-detail', kwargs={'pk': self.pk})

class Fiche(models.Model):
    LIMPIDITE = [
        ('trouble','Trouble'),
        ('brillant','Brillant'),
        ('scintillant','Scintillant')
    ]
    limpidite = models.CharField(max_length=20, choices=LIMPIDITE,default='brillant',verbose_name= 'Limpidité')
    INTENSITE_COULEURS = [
        ('pâle','Pâle'),
        ('moyenne','Moyenne'),
        ('profonde','Profonde'),
        ('foncée','Foncée'),
        ('soutenue','Soutenue')
    ]
    intensite_couleurs = models.CharField(max_length=20, choices=INTENSITE_COULEURS,default='moyenne', verbose_name= 'Intensité des couleurs')
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
    robe_blanc = models.CharField(max_length=20, choices=ROBE_BLANC, blank=True, null=True, verbose_name= 'Robe (blanc)')
    ROBE_ROSE = [
        ('gris','Gris'),
        ('rosé','Rosé'),
        ('rosé framboise','Rosé framboise'),
        ('rosé orange','Rosé orange')
    ]
    robe_rose = models.CharField(max_length=20, choices=ROBE_ROSE, blank=True, null=True, verbose_name= 'Robe (rosé)')
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
    robe_rouge = models.CharField(max_length=20, choices=ROBE_ROUGE, blank=True, null=True, verbose_name= 'Robe (rouge)')
    VISCOSITE = [
        ('léger','Léger'),
        ('normal','Normal'),
        ('lourd','Lourd'),
        ('gras','Gras')
    ]
    viscosite = models.CharField(max_length=20, choices=VISCOSITE, verbose_name= 'Viscosité')
    commentaires_visuel = models.TextField(verbose_name= 'Commentaires (visuel)', blank=True, null=True)
    INTENSITE_NEZ = [
        ('défectueux','Défectueux'),
        ('faible','Faible'),
        ('modéré','Modéré'),
        ('marqué','Marqué'),
        ('puissant','Puissant')
    ]
    intensite_nez = models.CharField(max_length=20, choices=INTENSITE_NEZ, verbose_name= 'Intensité du nez')
    RAPPEL = [
        ('nul','Nul'),
        ('léger','Léger'),
        ('moyen','Moyen'),
        ('distinct','Distinct'),
        ('prononcé','Prononcé')
    ]
    rappel_fruit = models.CharField(max_length=20, choices=RAPPEL, verbose_name= 'Rappel du fruit')
    rappel_floral = models.CharField(max_length=20, choices=RAPPEL, verbose_name= 'Rappel floral')
    rappel_epice = models.CharField(max_length=20, choices=RAPPEL, verbose_name= 'Rappel d\'épice')
    BOUQUET = [
        ('ordinaire','Ordinaire'),
        ('agréable','Agréable'),
        ('fin','Fin'),
        ('complexe','Complexe'),
        ('expressif','Expresssif')
    ] 
    bouquet = models.CharField(max_length=20, choices=BOUQUET)
    commentaires_arome = models.TextField(verbose_name= 'Commentaires (arôme)', blank=True, null=True)
    DOUCEUR = [
        ('extra-sec','Extra-sec'),
        ('sec','Sec'),
        ('demi-sec','Demi-sec'),
        ('moelleux','Moelleux'),
        ('liquoreux','Liquoreux')
    ]
    douceur = models.CharField(max_length=20, choices=DOUCEUR, blank=True, null=True, verbose_name= 'Douceur (blanc)')
    TANINS = [
        ('maigre','Maigre'),
        ('fondu','Fondu'),
        ('savoureux','Savoureux'),
        ('présent','Présent'),
        ('astringent','Astringent'),
        ('rude','Rude')
    ]
    tanins = models.CharField(max_length=20, choices=TANINS, blank=True, null=True, verbose_name= 'Tanins (rouge)')
    ACIDITE = [
        ('plat','Plat'),
        ('mou','Mou'),
        ('souple','Souple'),
        ('frais','Frais'),
        ('vif','Vif'),
        ('acide','Acide'),
        ('vert','Vert')
    ]
    acidite = models.CharField(max_length=20, choices=ACIDITE, verbose_name= 'Acidité')
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
    equilibre = models.CharField(max_length=20, choices=EQUILIBRE, verbose_name= 'Équilibre')
    commentaires_saveur = models.TextField(verbose_name= 'Commentaires (saveur)', blank=True, null=True)
    STADE_MATURATION = [
        ('passé','Passé'),
        ('vieilli','Vieilli'),
        ('épanoui','Epanoui'),
        ("s'ouvre", "S'ouvre"),
        ('fermé','Fermé')
    ]
    stade_maturation = models.CharField(max_length=20,choices=STADE_MATURATION, verbose_name= 'Stade de maturation')
    IMPRESSION_TECHNIQUE = [
        ('médiocre','Médiocre'),
        ('acceptable','Acceptable'),
        ('correct','Correct'),
        ('bon','Bon'),
        ('très bon', 'Très bon'),
        ('remarquable','Remarquable')
    ]
    impression_technique = models.CharField(max_length=20,choices=IMPRESSION_TECHNIQUE)
    commentaires_ensemble = models.TextField(verbose_name= 'Commentaires (ensemble)', blank=True, null=True)
    IMPRESSION_PERSONNELLE=[
        ('quelconque','Quelconque'),
        ('satisfaisant','Satisfaisant'),
        ('bien','Bien'),
        ('très bien','Très bien')
    ]
    impression_personnelle = models.CharField(max_length=20, choices=IMPRESSION_PERSONNELLE)
    date_degustation = models.DateField(default=timezone.now, verbose_name= 'Date de dégustation')
    periode_garde = models.CharField(max_length=20, verbose_name= 'Période de garde')
    vin = models.ForeignKey(Vin, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('fiche-detail', kwargs={'pk': self.pk})
