from django.contrib import admin
from .models import Manufacturer, Car, Driver
# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Driver)