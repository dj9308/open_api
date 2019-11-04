from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home/square/<int:width>/<int:height>',views.square),
    path('home/introduce/<name>/<int:age>/', views.introduce),
    path('home/hello/<name>/', views.hello),
    path('home/dinner/', views.dinner),
    path('home/lotto/', views.lotto),
    path('home/lotto2/', views.lotto2),
    path('home/hola/', views.hola),
    path ('home/index/', views.index),
    path('admin/', admin.site.urls),
]
