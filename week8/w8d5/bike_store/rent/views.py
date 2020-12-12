from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.core.exceptions import *
import pandas as pd
from rent.models import Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate
from .forms import AddCustomerForm, AddVehicleForm, AddRentalForm


def home_page(request):
    return render(request, 'rent/bike_homepage.html')


def all_rentals(request):
    rentals = Rental.objects.all()
    context = dict(rentals=rentals)
    return render(request, 'rent/rentals.html', context)


def rental_detail(request, id):
    try:
        rental = Rental.objects.get(id=id)
        return render(request, 'rent/rental.html', {"rental": rental})
    except ObjectDoesNotExist:
        return render(request, 'rent/rent404page.html')

# def rental_history(request,id):
#     rental_history = Rental.objects.filter(id = customer.id)
#     pass


def rental_add(request):
    if request.method == "GET":
        form = AddRentalForm()
        return render(request, 'rent/add_rental.html', {"form": form})


    if request.method == "POST":
        form = AddRentalForm(request.POST)

        if form.is_valid:
            form.save()
    return redirect('all_rentals')




def customer_id(request, id):
    try:
        customer = Customer.objects.get(id=id)
        rental_hist = Rental.objects.filter(id=customer.id)
        context = {
            "customer": customer,
            "rental_hist": rental_hist,
        }
        return render(request, 'rent/customer.html', context)
    except ObjectDoesNotExist:
        return render(request, 'rent/rent404.html')


def all_customers(request):
    customers = Customer.objects.all()
    return render(request, 'rent/customers.html', {'customers': customers})


def customers_add(request):
    if request.method == "GET":
        form = AddCustomerForm()
        return render(request, 'rent/add_customer.html', {"form": form})

    if request.method == "POST":
        form = AddCustomerForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('all_customers')


def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'rent/vehicles.html', {"vehicles": vehicles})


def vehicle_id(request, id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request, 'rent/vehicle.html', {'vehicle': vehicle})


def vehicle_add(request):
    if request.method == "GET":
        form  = AddVehicleForm()
        return render(request, 'rent/add_vehicle.html', {'form': form})

    if request.method == "POST":
        form = AddVehicleForm(request.POST)

        if form.is_valid:
            form.save()
        
    return redirect('vehicles')




# /rent/rental/ - show a list of all rentals, unreturned first, then ordered by date ascending (earliest first)
# /rent/rental/<pk> - show the information about the given rental:
# customer details
# vehicle details
# rental details (“Returned on: ” / “Not yet returned”)

# /rent/rental/add – allow you to enter a customer ID and a vehicle ID to create a rental.
# If the customer or the vehicle does not exist, show a user-friendly error message.
# If the vehicle is currently being rented, show a relevant error message.

# /rent/customer/<pk> - show the customer matching the given ID
# /rent/customer/ - show all customers, in alphabetical order
# /rent/customer/add – provide a form to add a new customer
# /rent/vehicle/ - show all vehicles, grouped into their groups (‘bike’ and ‘scooter’)
# /rent/vehicle/<pk> - show the specific vehicle
# also show whether it’s currently being rented
# /rent/vehicle/add – provide a
