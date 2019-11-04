from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk','title','title_en','audience','open_date','genre','watch_grade','score','poster_url','description')

#테이블 형태로 표현시켜줌.
admin.site.register(Movie, MovieAdmin)