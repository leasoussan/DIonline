from django.urls import path
from . import views


urlpatterns =[
    
    path('', views.HomeView.as_view(), name = "homepage"),
    path('add_film/', views.AddFilm.as_view(), name = "add_film"),
    path('add_director/', views.AddDirector.as_view(), name = "add_director"),
    # path('update_director/<int:pk>/', views.UpdateDirector.as_view(), name = "update_director"),

]