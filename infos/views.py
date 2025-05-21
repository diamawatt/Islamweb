from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q
import random

from .models import Article, Banner
from prayers.models import PrayerTime


def get_active_banners(category=None):
    today = timezone.now().date()
    banners = Banner.objects.filter(
        is_active=True,
        start_date__lte=today
    ).filter(
        Q(end_date__gte=today) | Q(end_date__isnull=True)
    )
    if category:
        banners = banners.filter(category=category)
    return list(banners)


def home(request):
    category = request.GET.get('category', None)

    banners = get_active_banners(category)
    banner = random.choice(banners) if banners else None

    articles_list = Article.objects.order_by('-published_at')
    paginator = Paginator(articles_list, 11)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    last_two_articles = articles_list[:4]

    context = {
        'banner': banner,
        'page_obj': page_obj,
        'last_two_articles': last_two_articles,
    }

    return render(request, 'infos/home.html', context)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    last_two_articles = Article.objects.order_by('-published_at')[:4]

    # Bannière générale (sans filtre catégorie)
    banners = get_active_banners()
    banner = random.choice(banners) if banners else None

    context = {
        'article': article,
        'last_two_articles': last_two_articles,
        'banner': banner,
    }

    return render(request, 'infos/article_detail.html', context)


def articles_by_category(request, category_name):
    today = timezone.now().date()

    if category_name.lower() == 'tous':
        articles = Article.objects.order_by('-published_at')
        banners = get_active_banners()
    else:
        articles = Article.objects.filter(category__iexact=category_name).order_by('-published_at')
        banners = Banner.objects.filter(
            is_active=True,
            start_date__lte=today
        ).filter(
            Q(end_date__gte=today) | Q(end_date__isnull=True)
        ).filter(
            Q(category__iexact=category_name) | Q(category__isnull=True)
        )
        banners = list(banners)

    banner = random.choice(banners) if banners else None

    paginator = Paginator(articles, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    last_two_articles = Article.objects.order_by('-published_at')[:2]

    context = {
        'page_obj': page_obj,
        'last_two_articles': last_two_articles,
        'current_category': category_name,
        'banner': banner,
    }

    return render(request, 'infos/home.html', context)


def article_search(request):
    query = request.GET.get('q')
    results = Article.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).order_by('-published_at') if query else []


    banners = get_active_banners()
    banner = random.choice(banners) if banners else None

    context = {
        'query': query,
        'results': results,
        'banner': banner,
    }

    return render(request, 'infos/search_results.html', context)


def get_last_friday(today):
    days_since_friday = (today.weekday() - 4) % 7
    return today - timedelta(days=days_since_friday)


def prayer_times_view(request):
    today = datetime.now().date()
    reference_day = get_last_friday(today)

    try:
        prayer_times = PrayerTime.objects.get(day=reference_day)
    except PrayerTime.DoesNotExist:
        prayer_times = None

    banners = get_active_banners()
    banner = random.choice(banners) if banners else None

    context = {
        'prayer_times': prayer_times,
        'reference_day': reference_day,
        'banner': banner,
    }

    return render(request, 'prayers/prayer_times.html', context)

