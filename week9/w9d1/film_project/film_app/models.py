from django.db import models
import datetime
from django.urls import reverse 
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"{self.name}"
    
    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"{self.name}"

    
    def __str__(self):
        return f"{self.name}"


class Director(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Film(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateField(auto_now = True)
    created_in_country = models.ForeignKey(Country, on_delete = models.CASCADE)
    available_in_countries = models.ManyToManyField(Country, related_name="availability_countires")
    category= models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)



    def __str__(self):
        return f"{self.title}{self.release_date}{self.created_in_country}{self.available_in_countries}{self.category}{self.director}"



