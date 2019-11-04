from django.shortcuts import render
from .models import Pastlife
from faker import Faker

# Create your views here.
def index(request):
    if request.method=='POST':
        faker = Faker()
        Original_name = request.POST.get('name')
        if(Pastlife.objects.get(Original_name=Original_name) == None):
            name = faker.name()
            address = faker.address()
            job = faker.job()
            pastlife = Pastlife(Original_name=Original_name, name=name, address=address, job=job)
            pastlife.save()
            
        pastlife = Pastlife.objects.get(Original_name=Original_name)
        return render(request, 'pastlife/answer.html',{'pastlife':pastlife})
    else:
        return render(request,'pastlife/index.html')
    