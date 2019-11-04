from django.contrib import admin
from .models import Pastlife

class PastlifeAdmin(admin.ModelAdmin):
    list_display = ('pk','name','address','job')

#테이블 형태로 표현시켜줌.
admin.site.register(Pastlife, PastlifeAdmin)