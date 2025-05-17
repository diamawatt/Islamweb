from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article

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
