from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


def index(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.all()
    # [::-1]
    return render(request, 'articles/index.html', {'articles':articles})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 사용자가 ArticleForm 으로 보낸 데이터를 받아서 form이라는 인스턴스를 받게해주는 것
        # form의 tpye는 ArticleForm이라는 클래스의 인스턴스(request.POST는 ...)
        if form.is_valid(): # form이 유효한지 체크한다.
            # form.cleaned_data 데이터를 요청받은대로 처리한다.
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # cleaned_data 지정해둔 데이터로 잘 들어오는지 확인한 후 받아옴.
            article = Article.objects.create(title=title,content=content)
            return redirect('articles:index')
    else:
        form = ArticleForm()
        # 상황에 따라 context에 넘어가는 2가지 form
        # 1. GET : 기본 form으로 넘겨짐
        # 2. POST: 검증에 실패(is_vaild->False)한 form(오류 메세지를 포함할 경우)
        return render(request, 'articles/new.html', {'form':form})
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()


#댓글에도 pk가 생기니까 그냥 pk가 아닌 article_pk인 것.
def detail(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk) 
    return render(request,'articles/detail.html',{'article':article})

def delete(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article_pk)

def update(request, article_pk):
    article = get_object_or_404(article, pk=article_pk)
    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect('articles:detail', article.pk)
        else:
            # ArticleForm 을 초기화(이전에 DB에 저장된 데이터 입력값을 넣어준 상태)
            form = ArticleForm(initial={'title':article.title, 'content':article.content})
            # form = ArticleForm(initial=article.__dict__) # 딕셔너리 자료형이 되어 저장
        return render(request, 'articles/new.html', {'form':form})
