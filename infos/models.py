from django.db import models
from django.utils import timezone

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('tous', 'Tout'),
        ('orient', 'Orient'),
        ('afrique', 'Afrique'),
        ('europe', 'Europe'),
        ('amerique', 'Amérique'),
        ('monde', 'Monde'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='afrique')

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.CharField(max_length=100, help_text="Titre descriptif de la bannière")
    image = models.ImageField(upload_to='banners/')
    url = models.URLField(blank=True, null=True, help_text="Lien sur lequel la bannière redirige")
    category = models.CharField(max_length=50, blank=True, null=True,
                                help_text="Catégorie ciblée (ex: Monde, Afrique, etc.)")
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True,
                                help_text="Date de fin d'affichage (optionnel)")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def is_current(self):
        today = timezone.now().date()
        if self.end_date:
            return self.is_active and self.start_date <= today <= self.end_date
        return self.is_active and self.start_date <= today