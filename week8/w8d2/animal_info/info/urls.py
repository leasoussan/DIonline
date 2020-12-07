from django.urls import path
from . import views 

urlpatterns = [
    path('', views.animals, name ='info_homepage'),
    path('animals', views.animals, name ='info_animals'),
    path('animal/<int:id>', views.animal, name ='info_animal'),
    path('family/<int:id>', views.family, name ='info_family')
    
    

]