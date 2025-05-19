from django.db import models


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

