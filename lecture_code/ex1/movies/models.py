from django.db import models

# Create your models here.
class Genre(models.Model):
    title = models.ForeignKey