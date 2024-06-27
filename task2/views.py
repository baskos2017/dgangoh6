from django.shortcuts import render
from .models import Manufacturer, Car, Driver

def filter_examples(request):
    # Отримання параметрів GET-запиту
    year = request.GET.get('year', None)
    age = request.GET.get('age', None)
    manufacturer_name = request.GET.get('manufacturer_name', None)
    car_model = request.GET.get('car_model', None)
    
    # Фільтрація даних на основі GET-параметрів
    cars = Car.objects.all().order_by('-created_at')
    drivers = Driver.objects.all().order_by('-created_at')
    manufacturers = Manufacturer.objects.all().order_by('-created_at')

    if year:
        cars = cars.filter(year__exact=year)
    
    if age:
        drivers = drivers.filter(age__exact=age)
    
    if manufacturer_name:
        manufacturers = manufacturers.filter(name__icontains=manufacturer_name)
    
    if car_model:
        cars = cars.filter(model__icontains=car_model)
    
    context = {
        'cars': cars,
        'drivers': drivers,
        'manufacturers': manufacturers,
    }
    return render(request, 'task2/filter_examples.html', context)
