from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from tablib import Dataset

from .import_data import VehicleResource
from .models import Vehicle



def simple_upload(request):
    if request.method == 'POST':
        vehicle_resource = VehicleResource()
        dataset = Dataset()
        new_vehicle = request.FILES['myfile']

        if not new_vehicle.name.endswith('xlsx'):
            messages.info(request, 'wrong file format')
            return render(request, 'propellers/upload.html')

        imported_data = dataset.load(new_vehicle.read(), format='xlsx')
        
        for data in imported_data:
            value = Vehicle(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6]
            )
            value.save()
    return render(request, 'propellers/upload.html')

class HomePageView(ListView):
    template_name = 'propellers/home.html'
    model = Vehicle
