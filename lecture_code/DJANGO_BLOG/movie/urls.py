from django.urls import path
from . import views

app_name = 'movie'

urlpatterns= [
    path('delete/<int:pk>',views.delete, name='delete'),
    path('<int:pk>/update/',views.update,name='update'),
    path('<int:pk>/detail',views.detail,name='detail'),
    path('create/',views.create, name='create'),
    path('',views.index, name='index'),
]
