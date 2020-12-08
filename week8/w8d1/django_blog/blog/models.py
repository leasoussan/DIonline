from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    content= models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __srt__(self):
        return f"{self.title}, Written on: {date_posted}" 