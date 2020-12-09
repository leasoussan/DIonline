from django.urls import path
from . import views 

urlpatterns = [
    path('phonenumber/<str:phone_number>', views.personinfo , name="person_by_number" ),
    path('name/<str:name>', views.nameinfo , name="person_by_name" ),
    path('search/', views.searchform , name="searchform" ),
    path('search_results/', views.searchform , name="search_results" ),

]
