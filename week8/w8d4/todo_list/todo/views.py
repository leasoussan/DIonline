from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import *
from django.http import Http404, HttpResponse
from todo.models import Todo, Category
from todo.forms import AddTodoForm


# Create your views here.

def todohome(request):
    if request.method == "GET":
        form = AddTodoForm()
        item_todo= Todo.objects.all()
        context = {
            "item_todo": item_todo,
            "form": form
        }
        return render(request, 'todo.html', context) 

    if request.method == "POST":
        form = AddTodoForm (request.POST)

        if form.is_valid():
            form.save()    
    
    return redirect('todohome') 



# def add_todo(request):

    
            
#         return redirect('todohome')
        


