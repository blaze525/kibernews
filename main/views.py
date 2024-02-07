from django.shortcuts import render
from . import models


def home(request):
    categories = []
    category = models.Category.objects.all()
    for i in range(100):
        categories += category
    news = models.News.objects.all()
    banners = models.Banner.objects.all()
    context = {
        'categories': categories,
        'news': news,
        'banners': banners,
        'range_100': range(101)
    }
    return render(request, 'home.html', context)


def news_detail(request, id):
    detail = models.News.objects.get(id=id)
    similar_news = models.News.objects.filter(category_id=detail.category.id)[:10]
    context = {
        'detail': detail,
        'similar_news': similar_news
    }
    return render(request, 'detail.html', context)


def news(request):
    category_id = request.GET.get('category_id')
    news = models.News.objects.all()
    category = None
    
    if category_id:
        try:
            category = models.Category.objects.get(id=int(category_id))
            news = news.filter(category_id=category_id)
        except models.Category.DoesNotExist:
            pass
    
    context = {
        'news': news,
        'category': category
    }
    
    return render(request, 'news.html', context)