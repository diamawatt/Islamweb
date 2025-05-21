from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category_name>/', views.articles_by_category, name='articles_by_category'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('recherche/', views.article_search, name='article_search'),


]
