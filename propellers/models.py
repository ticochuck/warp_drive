from django.db import models
from django.urls import reverse

class Vehicle(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    vehicle_type = models.CharField(max_length=64)
    prop_orientation = models.CharField(max_length=64)
    notes = models.CharField(max_length=64)


    def __str__(self):
        return f'{self.name}, {self.manufacturer}, {self.model}'


    def get_absolute_url(self):
        return reverse('home')
    

