# This file contains all the controllers for handling the models and creating the view.
# Each function that returns render() is associated with a url and handles HTTP requests from that url.
# These functions interact with the database through django's ORM and returns HTML pages for the user.


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

import datetime
import math

from .models import *

# Function that displays customers and employees
@login_required(login_url='/login')
def search_employee(request) :
    context = {}

    # grab all employees and customers
    context['employees'] = Employee.objects.all()
    customers = User.objects.filter(is_superuser=False)
    amount = []

    # Grab total purchase amount made by each customer
    for c in customers :
        amount.append(VehicleSale.objects.raw(f"""select SUM(sale_price) as sum, id from vehiclemanagement_vehiclesale
            where customer_id = {c.id}""")[0].sum)

    context['customers'] = zip(customers, amount)


    return render(request, 'vehiclemanagement/find-employee.html', context)

# Function that displays all vehicles in the database
@login_required(login_url='/login')
def search_vehicle(request) :
    context = {}
    
    # grab all vehicles in database
    vehicles = Vehicle.objects.all()

    # Handle filter form
    if request.method == 'POST' :
        context['checked'] = request.POST.get('sold')

        if request.POST.get('type') != 'none':
            context['type'] = request.POST.get('type')

        # filter vehicles based on form input
        if request.POST.get('sold') == 'on':
            vehicles = vehicles.filter(is_sold=True)
        else :
            vehicles = vehicles.filter(is_sold=False)
    
        if request.POST.get('type') != 'none':
            vehicles = vehicles.filter(vehicle_model__vehicle_type=context['type'])

    # pass vehicles to html page and order them from low to high price
    context['vehicles'] = vehicles.order_by('price')

    return render(request, 'vehiclemanagement/find-vehicle.html', context)

# logs user in
def login_(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser: # ensure user is an employee
            login(request, user)
            return redirect('/')
        else :
            messages.info(request, 'Username or password not found')

    return render(request, 'vehiclemanagement/login.html', {})

# create a customer or employee
# must be done by a logged in user
@login_required(login_url='/login')
def register(request) :

    # redirects user if they input a user id as a query param in url
    if request.method == 'PATCH' :
        return redirect('/register/' + request.PATCH.get('user') + '/')
    context = {}

    # grab user from url param, if there is one, and pass information to html page for form data
    if request.method == 'GET' :
        u = request.GET.get('user', '')

        if u != '' :
            context['curruser'] = get_object_or_404(User, pk=u)

        if request.method != 'POST':
            context['departments'] = Department.objects.all()
            context['employees'] = Employee.objects.all()

    # handle reqeust to create a new customer or employee
    if request.method == 'POST':
        u = None
        try :
            u = User.objects.get(id=request.POST.get('id'))
        except :
            u = None

        # grab column data for auth_user table and put into dictionary (map)
        userArgs = {
            'first_name': request.POST.get('firstname').lower(),
            'last_name': request.POST.get('lastname').lower(),
            'email': request.POST.get('email').lower(),
            'username': request.POST.get('username').lower()
        }
        user = None
        # if passwords match, create new user
        if request.POST.get('password1') == request.POST.get('password2'):
            if u is None:
                user = User.objects.create_user(request.POST.get('username').lower(), request.POST.get('email').lower(), request.POST.get('password1'))
                user = update_model(user, userArgs)
            elif u is not None :
                user = get_object_or_404(User, pk=u.id)
                user.set_password(request.POST.get('password1'))
                user = update_model(user, userArgs)
        else :
            return redirect('/register/')

        # if registering an employee, create a new employee
        if request.POST.get('usertype') == 'Employee' :
            # grab form data and put into dictionary
            empArgs = {
                'user': user,
                'SSN': request.POST.get('SSN'),
                'birthday': request.POST.get('birthday'),
                'phone_number': request.POST.get('phonenumber'),
                'sex': request.POST.get('sex'),
                'salary': request.POST.get('salary'),
                'total_commissions': 0,
            }

            if request.POST.get('department') != 'none' :
                empArgs['employee_department'] = get_object_or_404(Department, pk=request.POST.get('department'))
            if request.POST.get('manager') != 'none' :
                empArgs['manager'] = get_object_or_404(Employee, pk=request.POST.get('manager'))

            # create or update employee model
            if u is None :
                update_model(Employee(), empArgs)
                update_model(user, { 'is_superuser': True })
            elif u is not None :
                update_model(get_object_or_404(Employee, pk=u.id), empArgs)

        return redirect('/login/')

    return render(request, 'vehiclemanagement/register.html', context)

# logs user out
def logout_user(request) :
    logout(request)  # django handles this

    return redirect('/login/')

# handles creation or updating of a vehicle model
@login_required(login_url='/login')
def create_or_update_vehicle(request) :
    # grab vehicle vin number from url query param
    if request.method == 'PATCH' :
        return redirect('/vehicle/' + request.PATCH.get('v') + '/')

    context = {}

    # send data for form to html page
    if request.method == 'GET':
        v = request.GET.get('v', '')
        if v != '':
            context['vehicle'] = get_object_or_404(Vehicle, vin_number=v)

    # handle create or update of vehicle
    if request.method == 'POST':
        v = None
        try :
            v = Vehicle.objects.get(vin_number=request.POST.get('old_vin'))
        except :
            v = None

        # grab model args
        vehicleModelArgs = {
            'make': request.POST.get('make').lower(),
            'model': request.POST.get('model').lower(),
            'year': request.POST.get('year').lower(),
            'vehicle_type': request.POST.get('vehicle_type').lower()
        }

        # grab vehicle args
        vehicleArgs = {
            'vin_number': request.POST.get('vin_number'),
            'price': request.POST.get('price'),
            'color': request.POST.get('color'),
            'trim_level': request.POST.get('trim_level'),
            'is_sold': False,
            'mpg': request.POST.get('mpg'),
            'mileage': request.POST.get('mileage'),
            'description': request.POST.get('description')
        }
    
        # either select existing model or create new one
        vmodel = None
        try :
            vmodel = VehicleModel.objects.get(make=vehicleModelArgs['make'], model=vehicleModelArgs['model'],year=vehicleModelArgs['year'])
        except:
            vmodel = None
        if vmodel is None:
            vmodel = update_model(VehicleModel(), vehicleModelArgs)

        vehicleArgs['vehicle_model'] = vmodel
        image= None
        fss = None

        # save image to /media/ and save path to string for vehicle table
        try :
            image = request.FILES['pic']
            fss = FileSystemStorage()
        except:
            image = None
        if image is not None :
            file = fss.save(image.name, image)

            vehicleArgs['image'] = fss.url(file) 

        # insert vehicle or update
        if v is None :
            v = update_model(Vehicle(), vehicleArgs)
        else :
            v = update_model(v, vehicleArgs)

        # insert truck of car row
        if vehicleModelArgs['vehicle_type'] == 'truck' :
            truck = None
            try :
                truck = Truck.objects.get(vehicle=v)
            except :
                truck = Truck()

            truckArgs = {
                'vehicle': v,
                'bed_area': request.POST.get('bed_area'),
                'towing_capacity': request.POST.get('towing_capacity'),
            }

            update_model(truck, truckArgs)
        else :
            car = None
            try :
                car = Car.objects.get(vehicle=v)
            except :
                car = Car()

            carArgs = {
                'vehicle': v,
                'max_speed': request.POST.get('max_speed'),
                'no_of_seats': request.POST.get('no_of_seats'),
            }

            update_model(car, carArgs)

        return redirect('/searchvehicle/')

        

    return render(request, 'vehiclemanagement/add-vehicle.html', context)

# handle creation or updating of a sale
@login_required(login_url='/login')
def create_or_update_sale(request) :

    # grab url query param for sale_id
    if request.method == 'PATCH' :
        return redirect('/sale/' + request.PATCH.get('saleid') + '/')

    context = {}

    # grab data for form and send to html page
    if request.method == 'GET':
        v = request.GET.get('v', '')
        sale_id = request.GET.get('saleid', '')
        if v != '':
            context['vehicle'] = get_object_or_404(Vehicle, vin_number=v)
        if sale_id != '':
            context['sale'] = get_object_or_404(VehicleSale, pk=sale_id)

        context['employees'] = Employee.objects.all()
        context['today'] = datetime.datetime.today()

    # handle creation or update form
    if request.method == 'POST':
        sale_id = request.POST.get('old_sale')

        # grab column data from form
        vehicleSaleArgs = {
            'vehicle': get_object_or_404(Vehicle, vin_number=request.POST.get('vin_number')),
            'customer': get_object_or_404(User, username=request.POST.get('customer').lower()),
            'employee': get_object_or_404(Employee, user_id=request.POST.get('employee')),
            'sale_price': request.POST.get('sale_price'),
            'sale_date': request.POST.get('sale_date')
        }

        # update or create row
        if sale_id == '':
            update_model(VehicleSale(), vehicleSaleArgs)
        else :
            update_model(get_object_or_404(VehicleSale, pk=sale_id), vehicleSaleArgs)
        update_model(get_object_or_404(Vehicle, vin_number=request.POST.get('vin_number')), { 'is_sold': True })

        return redirect('/searchvehicle/')

    return render(request, 'vehiclemanagement/add-sale.html', context)

# home page controller
# gathers various stats to be displayed
@login_required(login_url='/login')
def index(request):
    context = {}
    today = datetime.date.today()
    curr_year = today.year
    curr_month = today.month

    # get current month's revenue for dashboard
    month_rev = VehicleSale.objects.raw(f"""select SUM(sale_price) as sum, id from vehiclemanagement_vehiclesale 
            where YEAR(sale_date) = {curr_year} and MONTH(sale_date) = {curr_month};""")[0].sum
    if month_rev is None :
        context['month_rev'] = 0
    else :
         context['month_rev'] = month_rev

    # get year's revenue for dashboard
    year_rev = VehicleSale.objects.raw(f"""select SUM(sale_price) as sum, id from vehiclemanagement_vehiclesale 
            where YEAR(sale_date) = {curr_year};""")[0].sum
    if year_rev is None :
        context['year_rev'] = 0
    else :
         context['year_rev'] = year_rev

    # get total salary cost for this month
    salary_cost = Employee.objects.raw(f"""select SUM(salary) as sum, user_id from vehiclemanagement_employee;""")[0].sum
    if salary_cost is None :
        context['salary_cost'] = 0
    else :
        context['salary_cost'] = salary_cost / 12

    # get total number of vehicles not sold yet
    inventory = Vehicle.objects.raw('select count(*) as count, vin_number from vehiclemanagement_vehicle where is_sold = false;')[0].count
    context['inventory'] = inventory

    return render(request, 'vehiclemanagement/index.html', context)

# gets revenue for each month and serializes it to json for jan-dec of current year
@login_required(login_url='/login/')
def get_revenue_chart_data(request):
    if request.method == 'GET':

        # ensure user can access this data
        if not(request.user.is_authenticated and request.user.is_superuser):
            return JsonResponse({})

        curr_year = datetime.date.today().year
        context = {}

        # get each months revenue
        for i in range(1, 13):
            c = VehicleSale.objects.raw(f"""select SUM(sale_price) as sum, id from vehiclemanagement_vehiclesale 
            where YEAR(sale_date) = {curr_year} and MONTH(sale_date) = {i};""")[0].sum

            if c == None :
                context[i] = "null"
            else :
                context[i] = c

        # return json of dictionary
        return JsonResponse(context)
    return JsonResponse({})

# updates or creates a model instance
def update_model(model, diction) :
    """
    Pass in a model to be added to db updated with dictionary of model attributes mapped to new value.
    If you are creating a new instance of a model, pass in an empty one. If you are updating a model, pass
    the existing model to be updated with a dictionary of changed model attributes. Returns the model in case
    the user needs it to complete others.
    """
    for key, value in diction.items() :
        setattr(model, key, value)
    model.save()

    return model
