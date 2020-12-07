from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.home, name= 'home'),
    path('people/<int:id>/', views.personId, name= 'personId'),
   

]
