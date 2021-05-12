import requests
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
        
        if form.is_valid():
            print('YOoOOOOOooOOOOOoooOOOO')
            engine = request.POST.get('engine_id')
            vehicle = request.POST.get('vehicle_id')
            reduction_rate = request.POST.get('reduction_ratio_rename_to_red_drive_name')
        
        database_info = Propeller.objects.all()
        # print(database_info[2])
        for result in database_info:
            if result.engine_id == 'Yamaha RX1':
                print('whasuuupppp')

        # for result in database_info:
        #     if result['engine_id'] == engine and result['vehicle_id'] == vehicle and result['reduction_ratio_rename_to_red_drive_name'] == reduction_rate:
        #         print(result)
            

        return redirect('home')

    else:
        form = SearchPropeller()

    context = {
        'form': form,
    }

    return render(request, 'propellers/search.html', context)
