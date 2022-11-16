from django.urls import path, re_path
from django.views.generic.base import RedirectView
from django.conf import settings
import os

from . import views

app_name = 'vehiclemanagement'

# holds all the urls and views they are associated with
urlpatterns = [
    path('login/', views.login_, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.index, name='index'),
    path('zzz/chart/', views.get_revenue_chart_data, name='revenue_chart'),
    path('vehicle/', views.create_or_update_vehicle, name='vehicle'),
    path('sale/', views.create_or_update_sale, name='sale'),
    path('searchvehicle/', views.search_vehicle, name='search_vehicle'),
    path('searchuser/', views.search_employee, name='search_employee'),
]