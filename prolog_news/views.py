from django.shortcuts import render
from django.views.generic import ListView
from .models import Arctik

from .models import Prolog_news


# Create your views here.

def news_pril(request):
    news = Prolog_news.object.all()
    return render(request, 'news/default.html', {'news': news})


class Content:
    pass


class Contents(ListView):
    md = Content
    templates = 'default.html'


def article_list(request):
    articles = Arctik.objects.order_by('-publication_date')[:10]
    context = {'articles': articles}
    return render(request, 'default.html', context)


