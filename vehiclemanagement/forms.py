from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Car, Department, Employee, Truck, Vehicle, VehicleModel, VehicleSale


class UserForm(forms.UserCreationForm):
    email = forms.EmailField(label = 'Email')
    fname = forms.CharField(label = 'First Name')
    lname = forms.CharField(label = 'Last Name')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
            'first_name', 'last_name')

        widgets = {
            # format: 'field': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'X'}),
        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee

        fields = ('ssn', 'birthday', 'phone_number', 'sex',
            'salary', 'department', 'manager')

class Department(ModelForm):
    class Meta:
        model = Department

        fields = ('department_name', 'department_manager')

class VehicleModel(ModelForm):
    class Meta:
        model = VehicleModel

        fields = ('make', 'model', 'year', 'vehicle_type')

class Vehicle(ModelForm):
    class Meta:
        model = Vehicle

        fields = ('vin_number', 'price', 'color', 'trim_level'
            'mpg', 'mileage', 'description')

class Car(ModelForm):
    class Meta:
        model = Car

        fields = ('trunk_area')

class Truck(ModelForm):
    class Meta:
        model = Truck

        fields = ('bed_area', 'number_of_axles')

class VehicleSale(ModelForm):
    class Meta:
        model = VehicleSale
        
        fields = ('sale_price', 'sale_date', 'employee', 'vehicle', 'customer')


