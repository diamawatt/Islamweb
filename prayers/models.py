from django.db import models

class PrayerTime(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField()    # Exemple : jeudi
    fajr = models.TimeField()
    dhuhr = models.TimeField()
    asr = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()

    def __str__(self):
        return f"Horaires du {self.start_date} au {self.end_date}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
