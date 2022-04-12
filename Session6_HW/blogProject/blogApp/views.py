from django.shortcuts import render, redirect 
from .models import Article
# Create your views here.
def new(request):
    if request.method =='POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
            # date : automatically written
        )
        return redirect('list')   
    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles})

def category(request, article_category):
    samecategory = Article.objects.filter(category=article_category)
    return render(request, 'category.html',
                  {'articles': samecategory,
                   'category': article_category})
def detail(request, article_id):
    # Get object from model
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', 
                  {'article_id':article_id,
                   'article':article,
                   })
