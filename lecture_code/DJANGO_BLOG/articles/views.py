from django.shortcuts import render, redirect
from .models import Article, Comment
def index(request):
    articles = Article.objects.order_by('-pk')
    # articles = Article.objects.all()[::-1]  # 콜론 두개면 뒤집는다는 뜻
    return render(request,'articles/index.html',{'articles':articles})

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    # article = Article(title=title, content=content)
    # article.save()

    # 3.
    # Article.objects.create(title=title, content=content)
        return redirect('articles:detail',article.article_id)
    else:
        return render(request,'articles/new.html')

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    comments = article.comment_set.all()
    return render(request, 'articles/detail.html',{'article':article, 'comments':comments})

def delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method=='POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.article_id)
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     return render(request, 'articles/edit.html', {'article':article})

def update(request, article_id):
    if request.method=='POST': 
        article = Article.objects.get(pk=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail',article.pk)
    else:
        article = Article.objects.get(pk=article_id)
        return render(request, 'articles/edit.html', {'article':article})

def comment_create(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method =='POST':
        comment = Comment()
        comment.article = article
        comment.content = request.POST.get('content')
        comment.save()
    return redirect('articles:detail',article_id)

def comment_delete(request, article_id, comment_id):
    if request.method=='POST':
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        return redirect('articles:detail', article_id)
