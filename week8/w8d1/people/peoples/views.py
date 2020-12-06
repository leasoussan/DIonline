from django.shortcuts import render
from django.http import HttpResponse


    


def home(request):
    people = [
    {
        'id': 1,
        'name': 'Bob Smith',
        'age': 35,
        'country': 'USA'
    },
    {
        'id': 2,
        'name': 'Martha Smith',
        'age': 60,
        'country': 'USA'
    },
    {
        'id': 3,
        'name': 'Fabio Alberto',
        'age': 18,
        'country': 'Italy'
    },
    {
        'id': 4,
        'name': 'Dietrich Stein',
        'age': 85,
        'country': 'Germany'
    }
    ]

    context = {
        "people": people,
    }
  
    return render(request, 'people.html', context)



def personId(request, id):
    people = home()

    for pers in people:

        context = {
            'id': pers.id,
            'name': pers.name,
            'age': pes.age,
            'country': pers.country
            }
    return render(request, 'people.html', context)