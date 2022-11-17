from django.contrib import admin

from .models import *

# Register models to be edited in /admin/ page
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(VehicleModel)
admin.site.register(Vehicle)
admin.site.register(VehicleSale)
admin.site.register(Car)
admin.site.register(Truck)