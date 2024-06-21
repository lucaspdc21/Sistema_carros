from django.shortcuts import render

from cars.models import Car

def cars_view (request):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
        #icontains ignora letras maiúsculas e minúsculas
        cars = Car.objects.filter(model__icontains=search)

    print(cars)
    return render(request, 'cars.html', {'cars' : cars})
