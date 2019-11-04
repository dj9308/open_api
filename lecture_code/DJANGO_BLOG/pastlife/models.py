from django.db import models

# Create your models here.
class Pastlife(models.Model):
    Original_name = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    address = models.TextField()
    job = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.name} : {self.address} : {self.job}'