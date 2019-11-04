from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def index(request):
    student = Student.objects.all()[::-1] 
    return render(request,'student/index.html',{'student':student})
    
def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/detail.html',{'student':student})

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('index')

def edit(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/edit.html', {'student':student})

def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.title = request.POST.get('title')
    student.content = request.POST.get('content')
    student.save()
    return redirect('student:detail',student.pk)