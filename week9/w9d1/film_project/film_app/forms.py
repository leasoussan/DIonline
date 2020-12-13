from django.forms import forms
from django.forms import ModelForm 
from .models import Film, Director 


class AddFilmForm(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'



class AddDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
