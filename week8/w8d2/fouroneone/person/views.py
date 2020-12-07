from django.shortcuts import render
from django.core.exceptions import *
from person.models import Person


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




# Create a view ‘/persons/phonenumber’ that will display all the info of person depending on his phone number
# Create a view ‘/persons/name’ that will display all the info of a person depending on his name.