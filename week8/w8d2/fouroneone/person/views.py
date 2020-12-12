from django.shortcuts import render, redirect
from django.core.exceptions import *
from person.models import Person
from django.db.models import Q
from person.forms import SearchPersonForm


def personinfo(request, phone_number):
    try:
        person_by_phone_number = Person.objects.get(phone_number= phone_number)
        context = dict(phone_number=person_by_phone_number)
        return render(request, 'person_number.html', context)
    
    except ObjectDoesNotExist:
        return render(request, '404page.html')




def nameinfo(request, name):
    try:
        person_by_name = Person.objects.get(name= name)
        context = dict(name=person_by_name)
        return render(request, 'person_name.html', context)


    except ObjectDoesNotExist:
        return render(request, '404page.html')


def searchform(request):
    if request.method == "GET":
        form = SearchPersonForm(request.POST)

        return render(request, 'search.html')

    if request.method == "POST":
        search_query = request.POST({'first_name':first_name,'last_name': last_name,'phone_number': phone_number})
        print(f"search query print: {search_query}")
        results = Person.objects.filter(first_name__icontains=request.POST["first_name"]) | Person.objects.filter(last_name__icontains=request.POST["first_name"]) | Person.objects.filter(phone_number__icontains=request.POST['phone_number'])
        print(results)
        
        context = {
            "form":form,
            "results" : results,
        }
        
        return render(request, 'search.html', context)



# def searchform(request):
#     if request.method == "GET":
#         form = SearchPersonForm(request.POST)

#         return render(request, 'search.html')

#     if request.method == "POST":
#         search_query = request.POST['first_name', 'last_name', 'phone_number']
#         results = Person.objects.filter(search_query__icontains=search_query[search_query])
        
#         context = {
#             "form":form,
#             "query_set" : query_set,
#         }
        
#         return render(request, 'search.html', context)