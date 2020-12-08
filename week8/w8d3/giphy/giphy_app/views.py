from django.shortcuts import render
from .models import Gif, Category


# Create your views here.


def home(request):
    gifs = Gif.objects.all() 
    category = Category.objects.all()
    context = {
        "gifs":gifs,
        "category": category,
    }
    return render(request, 'home.html', context)