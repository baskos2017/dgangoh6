from django.shortcuts import render
from .models import Manufacturer, Car, Driver

def filter_examples(request):
    # Приклади використання фільтрів

    # 1. in
    cars_in_2020_2021 = Car.objects.filter(year__in=[2020, 2021])

    # 2. gt (greater than)
    old_drivers = Driver.objects.filter(age__gt=30)

    # 3. gte (greater than or equal to)
    recent_cars = Car.objects.filter(year__gte=2018)

    # 4. lt (less than)
    young_drivers = Driver.objects.filter(age__lt=25)

    # 5. lte (less than or equal to)
    older_cars = Car.objects.filter(year__lte=2015)

    # 6. startswith
    manufacturers_startswith_toy = Manufacturer.objects.filter(name__startswith='Toy')

    # 7. endswith
    manufacturers_endswith_da = Manufacturer.objects.filter(name__endswith='da')

    # 8. range
    mid_age_drivers = Driver.objects.filter(age__range=(20, 30))

    # 9. isnull
    cars_without_driver = Car.objects.filter(drivers__isnull=True)

    # 10. regex
    manufacturers_regex = Manufacturer.objects.filter(name__regex=r'^[A-Z]')

    # 11. contains
    cars_contain_model = Car.objects.filter(model__contains='Model')

    # 12. exact
    exact_manufacturer = Manufacturer.objects.filter(name__exact='Toyota')

    context = {
        'cars_in_2020_2021': cars_in_2020_2021,
        'old_drivers': old_drivers,
        'recent_cars': recent_cars,
        'young_drivers': young_drivers,
        'older_cars': older_cars,
        'manufacturers_startswith_toy': manufacturers_startswith_toy,
        'manufacturers_endswith_da': manufacturers_endswith_da,
        'mid_age_drivers': mid_age_drivers,
        'cars_without_driver': cars_without_driver,
        'manufacturers_regex': manufacturers_regex,
        'cars_contain_model': cars_contain_model,
        'exact_manufacturer': exact_manufacturer,
    }
    return render(request, 'task2/filter_examples.html', context)
