from django.urls import path
from . import views

app_name = 'pastlife'

urlpatterns= [
    path('',views.index, name='index'),
]
