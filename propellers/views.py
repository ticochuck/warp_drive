import pandas as pd
from django_pandas.io import read_frame
import matplotlib.pyplot as plt

from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import SearchPropeller
from .models import Engine, Propeller, Vehicle


class HomePageView(ListView):
    template_name = 'propellers/home.html'
    model = Vehicle


class VehiclePageView(ListView):
    template_name = 'propellers/vehicles.html'
    model = Vehicle


class EnginePageView(ListView):
    template_name = 'propellers/engines.html'
    model = Engine


class PropellerPageView(ListView):
    template_name = 'propellers/propellers.html'
    model = Propeller


def search(request):

    if request.method == 'POST':
        form = SearchPropeller(request.POST)
        counter = 0
        if form.is_valid():
            if request.POST.get('engine_id') != '' or request.POST.get('engine_id') != None: 
                engine = request.POST.get('engine_id')
            if request.POST.get('vehicel_id') != '' or request.POST.get('vehicel_id') != None:
                vehicle = request.POST.get('vehicle_id')
            if request.POST.get('reduction_ratio_rename_to_red_drive_name') != '' or request.POST.get('reduction_ratio_rename_to_red_drive_name') != None:
                reduction_rate = request.POST.get('reduction_ratio_rename_to_red_drive_name')
                
            all_info = Propeller.objects.all()
            
            results = all_info

            if vehicle and engine and reduction_rate:
                results = results.filter(vehicle_id = vehicle)
                results = results.filter(engine_id = engine)
                results = results.filter(reduction_ratio_rename_to_red_drive_name = reduction_rate)
            elif vehicle and engine and not reduction_rate:
                results = results.filter(vehicle_id = vehicle)
                results = results.filter(engine_id = engine)
            if vehicle and reduction_rate and not engine:
                results = results.filter(vehicle_id = vehicle)
                results = results.filter(reduction_ratio_rename_to_red_drive_name = reduction_rate)
            elif vehicle:
                results = results.filter(vehicle_id = vehicle)
            elif engine and reduction_rate:
                results = results.filter(engine_id = engine)
                results = results.filter(reduction_ratio_rename_to_red_drive_name = reduction_rate)
            elif engine:
                results = results.filter(engine_id = engine)
            elif reduction_rate:
                results = results.filter(reduction_ratio_rename_to_red_drive_name = reduction_rate)

            # df = pd.DataFrame(results)

            # df = df['engine_id'].value_counts().head(5)

            
            qs = read_frame(results)

            most_common_engines = qs['engine_id'].value_counts().head(5)
            print(most_common_engines)
            
        context = {
            'results': results,
            'most_common_engines': most_common_engines
        }
        return render(request, 'propellers/results.html', context)

    else:
        form = SearchPropeller()

    context = {
        'form': form,
    }

    return render(request, 'propellers/search.html', context)
