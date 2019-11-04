from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.

def index(request):
    movie = Movie.objects.all()[::-1]
    return render(request,'movie/index.html',{'movie':movie})
    
def create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        score = request.POST.get('score')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movies = Movie(title=title, score=score, title_en=title_en, audience=audience,open_date=open_date, genre=genre,
        watch_grade=watch_grade,poster_url=poster_url, description=description)
        movies.save()
        return redirect('movie:index')
    else:
        return render(request,'movie/create.html')

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie/detail.html',{'movie':movie})


def update(request, pk):
    if request.method=='POST': 
        movie = Movie.objects.get(pk=pk)
        movie.title = request.POST.get('title')
        movie.score = request.POST.get('score')
        movie.title_en = request.POST.get('title_en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch_grade')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail',movie.pk)
    else:
        movie = Movie.objects.get(pk=pk)
        return render(request, 'movie/update.html', {'movie':movie})

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movie:index')