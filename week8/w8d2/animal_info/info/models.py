from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db import models


fs = FileSystemStorage(location='static/img')
# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=30)
        
    def __repr__(self):
        return self.name




class Animal(models.Model):
    name = models.CharField(max_length=30)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed =models.FloatField()
    photo = models.ImageField(upload_to='img/')
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    
    def __repr__(self):
        return self.name




