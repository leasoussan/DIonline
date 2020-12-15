from django.urls import path, include
from  .views import SigneUp


urlpatterns =[
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SigneUp.as_view(), name ='signup'),
    path('profile/', views.profile, name ='profile')
]