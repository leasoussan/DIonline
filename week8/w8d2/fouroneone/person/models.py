from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField(max_length = 254) 
    phone_number= PhoneNumberField() 
    address= models.CharField(max_length=250)

    def __repr__(self):
        return f"First Name: {self.name} Last Name: {self.last_name}"


        