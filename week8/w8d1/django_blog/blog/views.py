from django.shortcuts import render
from django.http import HttpResponse 
from .models import Post



def home(request):
    context= {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return HttpResponse('<h2> About blog</h2')