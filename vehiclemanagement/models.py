from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# Table that represents an employee
# Is a sub-entity of User table
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True , related_name='employee')
    SSN = models.IntegerField(unique=True)
    birthday = models.DateField()
    phone_number = models.BigIntegerField(unique=True)
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    salary = models.DecimalField(max_digits=11, decimal_places=2)
    total_commissions = models.DecimalField(max_digits=11, decimal_places=2)
    employee_department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL, related_name='employees')
    manager = models.ForeignKey('Employee', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

# Table that represents a department
class Department(models.Model):
    department_name = models.CharField(max_length=255, unique=True)
    department_manager = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, related_name='department')

    def __str__(self):
        return self.department_name

# table that holds information attributable and non-unique to a number of vehicles
class VehicleModel(models.Model):
    class Meta :
        constraints = [
            models.UniqueConstraint(fields=['make', 'model', 'year'], name='unique_vehiclemodel')
        ]
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    vehicle_type = models.CharField(max_length=63)

    def __str__(self):
        return '%s %s %d' % (self.make, self.model, self.year)

class Vehicle(models.Model):
    vin_number = models.CharField(max_length=17, primary_key=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    color = models.CharField(max_length=255)
    trim_level = models.CharField(max_length=63)
    is_sold = models.BooleanField(default=False)
    mpg = models.SmallIntegerField()
    mileage = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.TextField(null=True)
    vehicle_model = models.ForeignKey('VehicleModel', on_delete=models.RESTRICT, related_name='vehicles')

    def __str__(self):
        return self.vin_number

class Car(models.Model):
    vehicle = models.OneToOneField('Vehicle', primary_key=True, on_delete=models.CASCADE, related_name='car')
    trunk_area = models.FloatField()

    def __str__(self):
        return self.vehicle.vin_number

class Truck(models.Model):
    vehicle = models.OneToOneField('Vehicle', primary_key=True, on_delete=models.CASCADE, related_name='truck')
    bed_area = models.FloatField()
    number_of_axles = models.SmallIntegerField()

    def __str__(self):
        return self.vehicle.vin_number

class VehicleSale(models.Model):
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    sale_date = models.DateField(auto_now_add=True)

    employee = models.ForeignKey('Employee', on_delete=models.RESTRICT, related_name='employee_sales')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.RESTRICT, related_name='vehicle_sales')
    customer = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='customer_sales')

    def __str__(self):
        return '%s %s %s' % (self.employee, self.customer, self.vehicle)







