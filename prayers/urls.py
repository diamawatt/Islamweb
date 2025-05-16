from django.urls import path
from .views import prayer_times_view

urlpatterns = [
    path('', prayer_times_view, name='prayer_times'),
]
