from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import authenticate, login

# Create your views here.
class SigneUp(View):

    def get(self, request):
        return render(request, 'registration/signup.html')

    def post(self,request):

        form = UserCreationForm(request.POST)
        picture = request.POST['picture']
        dob = request.POST['dob']
        if form.is_valid():
            user = form.save()
            # after saving >> then creating a profile for the user 
            profile = Profile.objects.create(user= user,  picture= picture, dob=dob)
            # NOW WE HAVE A USER AND a profil we need to autenticate with clean data

            user= authenticate(form_cleaned_data['username'], form.cleaned_data['password1'], form.cleaned_data['password2'])

            if user is not None:
                login(request, user)
                return redirect('homepage')
        return redirect('signup')    




# Create your views here.




class LoginView(LoginView):
    template_name = "registration/login.html"

    def form_valid(self, form):
        user_to_authenticate = form.cleaned_data
        print(user_to_authenticate)
        return super().form_valid(form)



def profile(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    else:
        context ={}
        return render(request, 'registration/profile.html', context)


# def signup(request):
#     if request.method == "POST":
#         form =  UserCreationForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('homepage')
#     else: 
#         form =  UserCreationForm()

#     context = {"form":form}
#     return render(request, 'registration/signup.html', context )