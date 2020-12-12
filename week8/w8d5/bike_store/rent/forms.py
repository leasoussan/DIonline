from phone_field import PhoneField
from django.forms import forms
from django.forms import ModelForm
from .models import Customer, Vehicle, Rental


class AddCustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class AddVehicleForm(ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'


class AddRentalForm(ModelForm):

    class Meta:
        model = Rental
        fields = '__all__'
