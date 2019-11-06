from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at')

#테이블 형태로 표현시켜줌.
admin.site.register(Article, ArticleAdmin)