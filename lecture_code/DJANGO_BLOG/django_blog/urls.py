from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('movies/', include('movie.urls')),
    path('pastlife/', include('pastlife.urls')),
    path('student/', include('student.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
