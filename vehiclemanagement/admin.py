from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(VehicleModel)
admin.site.register(Vehicle)
admin.site.register(VehicleSale)
admin.site.register(Car)
admin.site.register(Truck)