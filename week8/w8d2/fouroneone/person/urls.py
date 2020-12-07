from django.urls import path
from . import views 

urlpatterns = [
    path('phonenumber/<str:phone_number>', views.personinfo , name="person_by_number" ),
    path('name/<str:name>', views.nameinfo , name="person_by_name" )
]
