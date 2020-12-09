from django import forms
from django.forms import ModelForm 

from person.models import Person 


class SearchPersonForm(ModelForm):
    class Meta:

        model = Person
        fields = ['first_name', 'last_name', 'phone_number']

