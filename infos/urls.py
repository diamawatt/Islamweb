from django.urls import path
from .views import home, article_detail, surahs_list

urlpatterns = [
    path('', home, name='home'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('surahs/', surahs_list, name='surahs_list'),
]
