from django.shortcuts import render
from .models import PrayerTime
from datetime import datetime

def prayer_times_view(request):
    today = datetime.now().date()

    all_days = PrayerTime.objects.values_list('day', flat=True)

    try:
        prayer_times = PrayerTime.objects.get(day=today)
    except PrayerTime.DoesNotExist:
        prayer_times = None

    return render(request, 'prayers/prayer_times.html', {
        'prayer_times': prayer_times,
        'today': today,
        'all_days': all_days,
    })
