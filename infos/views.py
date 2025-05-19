from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article
from prayers.models import PrayerTime
from datetime import datetime, timedelta


def home(request):
    articles_list = Article.objects.order_by('-published_at')
    paginator = Paginator(articles_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    last_two_articles = articles_list[:4]

    context = {
        'page_obj': page_obj,
        'last_two_articles': last_two_articles,
    }

    return render(request, 'infos/home.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    last_two_articles = Article.objects.order_by('-published_at')[:4]
    context = {
        'article': article,
        'last_two_articles': last_two_articles,
    }

    return render(request, 'infos/article_detail.html', context)

def articles_by_category(request, category_name):
    if category_name.lower() == 'tous':
        articles = Article.objects.order_by('-published_at')
    else:
        articles = Article.objects.filter(category__iexact=category_name).order_by('-published_at')

    paginator = Paginator(articles, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    last_two_articles = Article.objects.order_by('-published_at')[:2]

    return render(request, 'infos/home.html', {
        'page_obj': page_obj,
        'last_two_articles': last_two_articles,
        'current_category': category_name,
    })

from django.db.models import Q

def article_search(request):
    query = request.GET.get('q')
    results = Article.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).order_by('-published_at') if query else []
    return render(request, 'infos/search_results.html', {
        'query': query,
        'results': results,
    })

def get_last_friday(today):
    # .weekday() => lundi = 0, ..., vendredi = 4
    days_since_friday = (today.weekday() - 4) % 7
    return today - timedelta(days=days_since_friday)

def prayer_times_view(request):
    today = datetime.now().date()
    reference_day = get_last_friday(today)

    try:
        prayer_times = PrayerTime.objects.get(day=reference_day)
    except PrayerTime.DoesNotExist:
        prayer_times = None

    return render(request, 'prayers/prayer_times.html', {
        'prayer_times': prayer_times,
        'reference_day': reference_day,
    })

