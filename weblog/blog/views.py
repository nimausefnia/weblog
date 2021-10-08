from django.shortcuts import render,get_object_or_404
from .models import Article


def all_article(request):
    all_articles = Article.publish.all()
    return render(request, 'blog/all_article.html', {'all_articles': all_articles})


def article(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/article.html', {'article': article})
