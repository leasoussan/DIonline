from django.db import models
from django.contrib.auth.models import User 


# here we are importing the USER serving as basic login 
# from this we ll create the Profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.URLField(max_length=200)
    dob = models.DateField()