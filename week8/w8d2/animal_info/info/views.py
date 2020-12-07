from django.shortcuts import render
from info.models import Family, Animal


# Create your views here.

# def count_animal_per_fam(request):
#     animal_fam_count =  Animal.objects.filter(family = family).count()
#     return render(request,'family.html', {'animal_fam_count' : animal_fam_count})


def family(request, id):
    family = Family.objects.get(id =id)
    animals = Animal.objects.filter(family = family)
    animal_fam_count =  Animal.objects.filter(family = family).count()
    
    context  ={
       "family": family,
       "animals": animals, 
       "animal_fam_count": animal_fam_count,
    
    }

    return render(request, 'family.html', context)


def animals(request):
    animals = Animal.objects.all()
    context = dict(animals=animals)
    
    return render(request, 'animals.html', context)


def animal(request, id):
    animal = Animal.objects.get(id = id)
    context = {
        "animal": animal
    }
    
    return render(request, 'animal.html', context)

    


# def _getAnimals()




# /family/X, where X is the ID (primary key) of the given family. Should show a list of all animals in that family.
# /animal/X, where X is the ID (primary key) of the given animal. Should show all of the information about the given animal.
# /animals/ - should show a list of all the animals. When you click on any of the animals in the list, you should be taken to /animal/X (see above).