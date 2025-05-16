from django.db import models

# Create your models here.
from django.db import models

class PrayerTime(models.Model):
    day = models.DateField(unique=True)  # pour la date du vendredi
    fajr = models.TimeField()
    dhuhr = models.TimeField()
    asr = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()

    def __str__(self):
        return f"Heures de prière pour {self.day}"

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
