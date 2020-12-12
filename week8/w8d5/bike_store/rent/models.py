from django.contrib.auth.models import User
from django.db import models

import datetime
from phone_field import PhoneField


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class VehicleSize(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class VehicleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"



class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete = models.CASCADE)
    vehicle_date_created = models.DateField(auto_now=False)
    vehicle_real_cost = models.DecimalField(max_digits=9, decimal_places=2)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.vehicle_type}"


class Rental(models.Model):
    rental_date =models.DateField(auto_now=False)
    return_date =models.DateField(auto_now=False,null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    vehicle = models.ForeignKey(VehicleType, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.vehicle}"

class RentalRate(models.Model):
    rental_daily_rate = models.DecimalField(max_digits=9, decimal_places=2)
    rental_vehicle_type = models.ForeignKey(VehicleType, on_delete = models.CASCADE)
    rental_vehicle_size = models.ForeignKey(VehicleSize, on_delete = models.CASCADE) 

    def __str__(self):
        return f"{self.rental_daily_rate},{self.rental_vehicle_type}"