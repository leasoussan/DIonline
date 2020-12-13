from django.shortcuts import render, redirect
from django.views import generic
from .forms import AddFilmForm, AddDirectorForm
from .models import Film, Director, Category, Country
from django.views.generic.edit import UpdateView, CreateView

# Create your views here.

class HomeView(generic.ListView):
    model = Film
    template_name = 'homepage.html'


    # def get_context_data(self, **kwargs):
    
    #     context = super(Film, self).get_context_data(**kwargs)
    #      # Add context data to pass to template
    #     context['director'] = "Director"
    #     context['director'] = director
    #     return context



class AddFilm(CreateView):
    model = Film
    fields ='__all__'
    template_name = "films/add_film.html"
    success_url = "homepage"
    
    
    # def get(self, request):
    #     form = AddFilmForm()
    #     return render(request, 'films/add_film.html', {"form": form})

    # def post(self, request):
        
    #     form = AddFilmForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    #     return redirect('homepage')



class AddDirector(generic.View):
    def get(self, request):
        form = AddDirectorForm()
        return render(request, 'directors/add_director.html', {"form":form})

    def post(self, request):

        form = AddDirectorForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('homepage')   




# class UpdateDirector(UpdateView):
#     model = Director
#     template_name = 'update_director.html'
    

#     def get_success_url(self):
#         return reverse_lazy('homepage', kwargs={'pk': self.director_list.id})