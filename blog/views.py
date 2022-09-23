from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Article, Category
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='login')
def list(request):
    
    articles = Article.objects.all()
    # Establecer el número de artículos por página
    paginator = Paginator(articles, 2)
    # Obtener la página actual por url
    page = request.GET.get('page')
    # Guardar todos los articulos que hay en la página
    page_articles = paginator.get_page(page)
    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        # mostrar page_articles
        'articles': page_articles,
    })
# @login_required(login_url='login') 
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # articles = Article.objects.filter(categories=category_id)
    return render(request, 'categories/category.html',{
        'category': category,
        # 'articles': articles
    })
# @login_required(login_url='login')   
def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    return render(request, 'articles/detail.html', {
        'article': article
    })