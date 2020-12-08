from django.db import models
import datetime



# Create your models here.


class Gif(models.Model):
    title =models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return f"Title {self.title} ID: {self.id}"


class Category(models.Model):
    name = models.CharField(max_length=50)   
    gifs = models.ManyToManyField(Gif)    

    def __repr__(self):
        return f"Name {self.name}"
