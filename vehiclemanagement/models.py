# File that contains the clases that map to tables in the MySQL database
# Each class specifies the columns and constraints on those columns and django
# handles migrating changes to the database with the command manage.py makemigrations
# then manage.py migrate


from django.db import models

from django.contrib.auth.models import User

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

# table that represents a vehicle
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

# table that represents a car
# is a subentity of vehicle
class Car(models.Model):
    vehicle = models.OneToOneField('Vehicle', primary_key=True, on_delete=models.CASCADE, related_name='car')
    max_speed = models.SmallIntegerField(null=True)
    no_of_seats = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.vehicle.vin_number

# table that represents a truck
# is a subentity of vehicle
class Truck(models.Model):
    vehicle = models.OneToOneField('Vehicle', primary_key=True, on_delete=models.CASCADE, related_name='truck')
    bed_area = models.FloatField()
    towing_capacity = models.IntegerField(null=True)

    def __str__(self):
        return self.vehicle.vin_number

# represents a vehicle transaction where a vehicle is sold to a customer
class VehicleSale(models.Model):
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    sale_date = models.DateField(auto_now_add=True, db_index=True)

    employee = models.ForeignKey('Employee', on_delete=models.RESTRICT, related_name='employee_sales')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.RESTRICT, related_name='vehicle_sales')
    customer = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='customer_sales')

    def __str__(self):
        return '%s %s %s' % (self.employee, self.customer, self.vehicle)