from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk','name','email','age')

#테이블 형태로 표현시켜줌.
admin.site.register(Student, StudentAdmin)