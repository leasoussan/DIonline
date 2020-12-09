from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self):
        return self.name



URGENCY_CHOICES =( 
    ("1", "SUPER URGENT"), 
    ("2", "IMPORTANT"), 
    ("3", "ASAP"), 
    ("4", "CAN WAIT"), 
    ("5", "WHEN POSSIBLE"), 
)



class Todo(models.Model):
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    has_been_done = models.BooleanField()
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateTimeField(auto_now=True)
    deadline_date = models.DateField()
    category = models.ManyToManyField(Category)
    urgency = models.CharField(max_length=50, choices=URGENCY_CHOICES )

    def __str__(self):
        return self.title

