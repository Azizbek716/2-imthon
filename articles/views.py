from django.shortcuts import render, redirect, get_object_or_404
from .models import Article



def home(request):
    articles = Article.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)

def create_articles(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        title = request.POST.get('title')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        category = request.POST.get('category')
        if author_name and title and short_content and long_content and category:
            Article.objects.create(
                author_name=author_name,
                title=title,
                short_content=short_content,
                long_content=long_content,
                category=category,
            )
            return redirect('home')
    return render(request, 'articles/add-post.html')

def articles_by_category(request, category):
    articles = Article.objects.filter(category=category)
    ctx = {'articles': articles,
           'category': category}
    return render(request, 'articles/articles-by-category.html', ctx)

def articles_detail(request, pk):
    articles = get_object_or_404(Article, pk=pk)
    ctx = {'articles': articles}
    return render(request, 'articles/detail.html', ctx)
