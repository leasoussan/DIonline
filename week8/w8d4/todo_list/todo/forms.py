from django import forms
from django.forms import ModelForm
from todo.models import Todo, Category, URGENCY_CHOICES



class AddTodoForm(ModelForm):
    
    class Meta:
        model = Todo
        fields = '__all__'
        title = forms.CharField(max_length=50, widget=forms.Select(choices=URGENCY_CHOICES))
        # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())