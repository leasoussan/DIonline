from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name = "home_page"),
    path('rentals/', views.all_rentals, name = "all_rentals"),
    path('rental/<int:id>', views.rental_detail, name = "rental_detail"),
    path('rental/add', views.rental_add, name = "rental_add"),
    path('customer/<int:id>', views.customer_id, name = "customer_id"),
    path('customers/', views.all_customers, name = "all_customers"),
    path('customer/add/', views.customers_add, name = "customers_add"),
    path('vehicles/', views.vehicles, name = "vehicles"),
    path('vehicle/<int:id>', views.vehicle_id, name = "vehicle_id"),
    path('vehicle/add', views.vehicle_add, name = "vehicle_add"),
 ]


