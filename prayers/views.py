from django.shortcuts import render
from .models import PrayerTime
from datetime import datetime, time
from django.db.models import Q

def get_next_prayer(prayer_times):
    now = datetime.now().time()
    prayers_order = ['fajr', 'dhuhr', 'asr', 'maghrib', 'isha']

    for prayer_name in prayers_order:
        time_val = getattr(prayer_times, prayer_name)
        if not isinstance(time_val, time):
            time_val = datetime.strptime(str(time_val), "%H:%M:%S").time()

        if now < time_val:
            # Calcul du temps restant en minutes
            diff = datetime.combine(datetime.today(), time_val) - datetime.now()
            total_minutes = int(diff.total_seconds() // 60)
            hours, minutes = divmod(total_minutes, 60)
            remaining = f"{hours}h {minutes}min" if hours else f"{minutes}min"
            return {
                "name": prayer_name.capitalize(),
                "time": time_val.strftime("%H:%M"),
                "remaining": remaining
            }

    fajr_time = getattr(prayer_times, 'fajr')
    if not isinstance(fajr_time, time):
        fajr_time = datetime.strptime(str(fajr_time), "%H:%M:%S").time()

    return {
        "name": "Fajr",
        "time": fajr_time.strftime("%H:%M"),
        "remaining": "Demain Insha'Allah"
    }


def prayer_times_view(request):
    today = datetime.now().date()

    try:
        prayer_times = PrayerTime.objects.get(
            Q(start_date__lte=today) & Q(end_date__gte=today)
        )
    except PrayerTime.DoesNotExist:
        prayer_times = None

    next_prayer = get_next_prayer(prayer_times) if prayer_times else None

    return render(request, 'prayers/prayer_times.html', {
        'prayer_times': prayer_times,
        'today': today,
        'next_prayer': next_prayer,
    })
