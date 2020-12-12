import django
# os to interact with computer 
import os
from faker import Faker
import random
# setting the env 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
# this line will check for the setting to know where to save it 
django.setup()
# after the above step >> we can import models 
from rent.models import Customer


fake_c = Faker()


def populating_customers(n):
    for i in range(n):
        # generating fake data
        f_first_name = fake_c.name()
        f_last_name = fake_c.last_name()
        f_email = fake_c.email()
        f_phone_number = fake_c.phone_number()
        f_address = fake_c.address()
        f_city = fake_c.city()
        f_country = fake_c.city()

        
        # creating data object and saving to DB
        customer = Customer(
            first_name=f_first_name,
            last_name=f_last_name,
            email=f_email,
            phone_number=f_phone_number,
            address=f_address,
            city=f_city,
            country =f_country,
        )
        customer.save()
        print(f'Created Customer:{customer.id}')
    
    # finished
    print(f"Finished...{n} entries populated.")


populating_customers(50)
