from django.contrib import admin
from .models import PrayerTime, Article, PrayerTime

@admin.register(PrayerTime)
class PrayerTimeAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'fajr', 'dhuhr', 'asr', 'maghrib', 'isha']



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('published_at',)


