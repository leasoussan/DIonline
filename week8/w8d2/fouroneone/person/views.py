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

    form = SearchPersonForm(request.POST or None)
    if request.method == "GET":

        query_set = Person.objects.filter(
                Q(first_name__icontains=form["first_name"]) & Q(last_name__icontains=form["first_name"]) | Q(phone_number__icontains=form['phone_number'])
            )
        
        context = {
            "form":form,
            "query_set" : query_set
        }
        return render(request, 'search.html', context)


    return redirect('searchform')    



def searchresults(request):
    


# Create two views: Daily challenge w8d4
# 1. One that uses a form to submit either a phone number or a name.
# Hint: For the form, use the PhoneNumberField that was provided for you by the django package: django-phonenumber-field.
# 2. The other one displays the results, if there are any available


# 84d2
# Create a view ‘/persons/phonenumber’ that will display all the info of person depending on his phone number
# Create a view ‘/persons/name’ that will display all the info of a person depending on his name.