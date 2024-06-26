from django.shortcuts import render

from cars.forms import NewCarForm
from cars.models import Car

def cars_view (request):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
        #icontains ignora letras maiúsculas e minúsculas
        cars = Car.objects.filter(model__icontains=search)

    print(cars)
    return render(request, 'cars.html', {'cars' : cars})

def new_car_view (request):
    add_car_form = NewCarForm()
    return render(request, 'add_car_form.html', {'car_form': add_car_form})