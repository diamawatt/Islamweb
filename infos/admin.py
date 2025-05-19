from django.contrib import admin
from .models import Article, Banner

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_at')
    list_filter = ('category',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'category')
    ordering = ('-start_date',)
