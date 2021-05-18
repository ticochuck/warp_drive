# import itertools

import matplotlib

matplotlib.use("Agg")

import base64
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django_pandas.io import read_frame
from pandas.core import groupby

from .forms import SearchPropeller
from .models import Engine, Propeller, Vehicle


def home(request):
    
    context = {
        'title': 'Home'
    }

    return render(request, 'propellers/home.html', context)


class VehiclePageView(ListView):
    template_name = 'propellers/vehicles.html'
    model = Vehicle


class EnginePageView(ListView):
    template_name = 'propellers/engines.html'
    model = Engine


class PropellerPageView(ListView):
    template_name = 'propellers/propellers.html'
    model = Propeller



def database_page(request):

    context = {
        'title': 'Databases'
    }

    return render(request, 'propellers/databases.html', context)

def search(request):

    if request.method == 'POST':
        form = SearchPropeller(request.POST)
        
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

            # create DataFrame
            qs = read_frame(results)
            
            # get top 5 most common engines
            most_common_engines_names = qs['engine_id'].value_counts()[:10].index.tolist()
            
            most_common_engines_totals = qs['engine_id'].value_counts()[:10].tolist()
            print(most_common_engines_totals)
            
            most_common_red_rates = qs['reduction_ratio_rename_to_red_drive_name'].value_counts().head(10)

            qs2 = results.values()
            data = pd.DataFrame(qs2).head(10)
            
        context = {
            'title': 'Results',
            'results': results,
            'most_common_engines_names': most_common_engines_names,
            'most_common_engines_totals': most_common_engines_totals,
            'most_common_red_rates': most_common_red_rates,
            'df': data.to_html()
        }
        return render(request, 'propellers/results.html', context)

    else:
        form = SearchPropeller()

    context = {
        'title': 'Search',
        'form': form,
    }
    
    return render(request, 'propellers/search.html', context)


def overall_stats(request):
    qs = Propeller.objects.all().filter(vehicle_id = 'un-Gyro').values()
    data = pd.DataFrame(qs).drop(['id', 'old_Serial', 'new_Serial', 'hub_Serial', 'status', 'product_id', 'do_not_import', 'hub_model', 'taper_specs', 'tip_color', 'weight_start', 'weight_end', 'weight_vert', 'weight_taperbefore', 'weight_taperafter', 'tracking', 'bld_notes', 'pinned_collars', 'customer_notes', 'vehicle_notes', 'engine_notes', 'bolt_pattern_notes_new_field', 'reduction_style', 'update_1_date', 'update_1', 'update_2_date', 'update_2', 'update_3_date', 'update_3', 'update_4_date', 'update_4', 'update_5_Date', 'update_5', 'x_studio_ship_date', 'old_notes', 'old_bldspecs', 'old_bldnum', 'old_bldtype', 'old_hub'], axis=1)
    
    data2 = pd.DataFrame(Propeller.objects.all().filter(vehicle_id = 'un-Gyro').values())
    
    d = data2.groupby('engine_id')['reduction_ratio_rename_to_red_drive_name'].count().sort_values(ascending=False).head(10)
    print('d', d)
    data2 = data2['engine_id'].value_counts().head(10)
       
    ts = Propeller.objects.all().filter(vehicle_id='Messerschmitt ME109')
    x = [x.engine_id for x in ts]
    
    y = [y.reduction_ratio_rename_to_red_drive_name for y in ts]
    plt.title('Engines and Red Rates')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Engines')
    plt.ylabel('Reduction Rates')
    plt.tight_layout()
    
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()


    context = {
        'title': 'Stats',
        'df': data.to_html(),
        'data2': data2,
        'd': d,
        'chart': image_base64
    }

    
    return render(request, 'propellers/overall_stats.html', context)
    

