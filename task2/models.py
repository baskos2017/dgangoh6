from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model

class Driver(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    cars = models.ManyToManyField(Car, related_name='drivers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
