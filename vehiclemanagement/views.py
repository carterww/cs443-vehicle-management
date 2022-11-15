from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

import datetime

from .models import *

# logs user in
def login_(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/')
        else :
            messages.info(request, 'Username or password not found')

    return render(request, 'vehiclemanagement/login.html', {})

# create a customer or employee
@login_required(login_url='/login')
def register(request) :
    if request.method == 'PATCH' :
        return redirect('/register/' + request.PATCH.get('user') + '/')
    context = {}
    if request.method == 'GET' :
        u = request.GET.get('user', '')

        if u != '' :
            context['curruser'] = get_object_or_404(User, pk=u)

        if request.method != 'POST':
            context['departments'] = Department.objects.all()
            context['employees'] = Employee.objects.all()

    if request.method == 'POST':
        u = None
        try :
            u = User.objects.get(username=request.POST.get('username'))
        except :
            u = None

        userArgs = {
            'first_name': request.POST.get('firstname'),
            'last_name': request.POST.get('lastname'),
            'email': request.POST.get('email'),
            'username': request.POST.get('username')
        }
        user = None
        if request.POST.get('password1') == request.POST.get('password2'):
            if u is None:
                user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password1'))
                user = update_model(user, userArgs)
            elif u is not None :
                user = get_object_or_404(User, pk=u.id)
                user.set_password(request.POST.get('password1'))
                user = update_model(user, userArgs)
        else :
            return redirect('/register/')

        if request.POST.get('usertype') == 'Employee' :
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

@login_required(login_url='/login')
def create_or_update_vehicle(request) :
    if request.method == 'PATCH' :
        return redirect('/vehicle/' + request.PATCH.get('v') + '/')

    context = {}

    if request.method == 'GET':


        v = request.GET.get('v', '')
        if v != '':
            context['vehicle'] = get_object_or_404(Vehicle, vin_number=v)

    if request.method == 'POST':
        v = None
        try :
            v = Vehicle.objects.get(vin_number=v)
        except :
            v = None

        vehicleModelArgs = {
            'make': request.POST.get('make'),
            'model': request.POST.get('model'),
            'year': request.POST.get('year'),
            'vehicle_type': request.POST.get('vehicle_type')
        }

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
    

        vmodel = None
        try :
            vmodel = VehicleModel.objects.get(make=vehicleModelArgs['make'], model=vehicleModelArgs['model'],year=vehicleModelArgs['year'])
        except:
            vmodel = None
        if vmodel is None:
            vmodel = update_model(VehicleModel(), vehicleModelArgs)

        vehicleArgs['vehicle_model'] = vmodel
        image = request.FILES['pic']
        fss = FileSystemStorage()
        file = fss.save(image.name, image)

        vehicleArgs['image'] = fss.url(file) 

        if v is None :
            v = update_model(Vehicle(), vehicleArgs)
        else :
            v = update_model(v, vehicleArgs)

        return redirect('/')

        

    return render(request, 'vehiclemanagement/add-vehicle.html', context)

@login_required(login_url='/login')
def create_or_update_sale(request) :
    context = {}

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
                context[i] == c

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
