from django.urls import path
from . import views

app_name = 'articles' # {% urls articles: %} 을 실행하기위해 적는 것.

urlpatterns=[
    path('<int:article_pk>/update/',views.update, name='update'),
    path('<int:article_pk>/delete',views.delete, name='delete'),
    path('<int:article_pk>/',views.detail,name='detail'),
    path('create/',views.create, name='create'),
    path('',views.index, name='index'),
]