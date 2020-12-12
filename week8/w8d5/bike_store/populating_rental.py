import django
import os
from faker import Faker
import random 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()
from rent.models import Rental, Customer, VehicleType



fakerental = Faker()


def pop_rental(n):
    for i in range(n):
        f_start_date = fakerental.date_between(start_date ='-100d', end_date ='-20d') 
        f_end_date = fakerental.date_between(start_date='-20d', end_date='now')
        customer = Customer.random.all()[0]
        vehicle = VehicleType.random.all()[0]

        print(f"{f_start_date}, {f_end_date}{customer}{vahicle}")



pop_rental(1)    