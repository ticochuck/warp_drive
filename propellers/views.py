# import matplotlib

# matplotlib.use('Agg')

# import base64
# from io import BytesIO

import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('ggplot')

import pandas as pd
# import seaborn as sns
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django_pandas.io import read_frame

from .forms import SearchPropeller
from .models import Engine, Propeller, Vehicle
from .plots import get_plot



class VehiclePageView(ListView):
    template_name = 'propellers/vehicles.html'
    model = Vehicle


class EnginePageView(ListView):
    template_name = 'propellers/engines.html'
    model = Engine


class PropellerPageView(ListView):
    template_name = 'propellers/propellers.html'
    model = Propeller


def home(request):
    
    context = {
        'title': 'Home'
    }

    return render(request, 'propellers/home.html', context)


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
                reduction_drive = request.POST.get('reduction_ratio_rename_to_red_drive_name')
            
            if  engine == '' and vehicle == '' and reduction_drive == '':
                
                message = 'When searching, you must enter information in at least 1 field'

                context = {
                    'title': 'Results',
                    'message': message,
                }
                
                # return redirect('search')
                return render(request, 'propellers/results.html', context)

            if vehicle and engine and reduction_drive:
                results = Propeller.objects.all().filter(vehicle_id__contains = vehicle)
                results = results.filter(engine_id__contains = engine)
                results = results.filter(reduction_ratio_rename_to_red_drive_name__contains = reduction_drive)
            elif vehicle and engine and not reduction_drive:
                results = Propeller.objects.all().filter(vehicle_id__contains = vehicle)
                results = results.filter(engine_id__contains = engine)
            elif vehicle and reduction_drive and not engine:
                results = Propeller.objects.all().filter(vehicle_id__contains = vehicle)
                results = results.filter(reduction_ratio_rename_to_red_drive_name__contains = reduction_drive)
            elif vehicle:
                results = Propeller.objects.all().filter(vehicle_id__contains = vehicle)
            elif engine and reduction_drive:
                results = Propeller.objects.all().filter(engine_id__contains = engine)
                results = results.filter(reduction_ratio_rename_to_red_drive_name__contains = reduction_drive)
            elif engine:
                results = Propeller.objects.all().filter(engine_id__contains = engine)
            else:
                results = Propeller.objects.all().filter(reduction_ratio_rename_to_red_drive_name__contains = reduction_drive)
            
            chart =  get_plot(results)

            message = 'No results found. Please try searching with different criteria'

            df = some_da(results)

            context = {
                'title': 'Results',
                'results': results,
                'message' : message,
                'chart': chart,
                'df': df
            }

        return render(request, 'propellers/results.html', context)

    else:
        form = SearchPropeller()

    context = {
        'title': 'Search',
        'form': form,
    }
    
    return render(request, 'propellers/search.html', context)


def some_da(results):

    df = pd.DataFrame(results)

    df = df.groupby(['engine_id', 'blade_count'])

    # df = pd.DataFrame(df)

    return df


def data_analysis(results):
    
    # create DataFrame
    qs = read_frame(results)
    df = pd.DataFrame(results)
    
    # get top 5 most common engines
    most_common_engines_names = qs['engine_id'].value_counts()[:10].index.tolist()
    
    most_common_engines_totals = qs['engine_id'].value_counts()[:10].tolist()
    
    most_common_red_drives = qs['reduction_ratio_rename_to_red_drive_name'].value_counts()[:10].tolist()

        
    # return graph


def overall_stats(request):
    qs = Propeller.objects.all().filter(vehicle_id = 'un-Gyro').values()
    
    filtered_data = pd.DataFrame(qs).drop(['id', 'old_Serial', 'new_Serial', 'hub_Serial', 'status', 'product_id', 'do_not_import', 'taper', 'hub_model', 'taper_specs', 'tip_color', 'weight_start', 'weight_end', 'nickel_LE', 'weight_vert', 'weight_taperbefore', 'weight_taperafter', 'tracking', 'bld_notes', 'pinned_collars', 'customer_notes', 'vehicle_notes', 'engine_notes', 'bolt_pattern_notes_new_field', 'reduction_style', 'update_1_date', 'update_1', 'update_2_date', 'update_2', 'update_3_date', 'update_3', 'update_4_date', 'update_4', 'update_5_Date', 'update_5', 'x_studio_ship_date', 'old_notes', 'old_bldspecs', 'old_bldnum', 'old_bldtype', 'old_hub'], axis=1)
    
    # filtered_data = read_frame(Propeller.objects.all().filter(vehicle_id='un-Gyro'))
    data = read_frame(Propeller.objects.all())
    most_common_engines = data['engine_id'].value_counts().head(10)
    most_common_engines = pd.DataFrame(most_common_engines)
    
    most_common_vehicles = data['vehicle_id'].value_counts().head(10)
    most_common_vehicles = pd.DataFrame(most_common_vehicles)
    
    most_common_red_drives = data['reduction_ratio_rename_to_red_drive_name'].value_counts().head(10)
    most_common_red_drives = pd.DataFrame(most_common_red_drives)

    # latest = read_frame(data)
    # latest = latest['datax_studio_ship_date']
    # print(latest)
    
    # x = [x.engine_id for x in ts]
    # y = [y.reduction_ratio_rename_to_red_drive_name for y in ts]

    context = {
        'title': 'Stats',
        'df': filtered_data.to_html(),
        'most_common_engines': most_common_engines.to_html(),
        'most_common_vehicles': most_common_vehicles.to_html(),
        'most_common_red_drives': most_common_red_drives.to_html(),
        # 'fig': fig
    }

    return render(request, 'propellers/overall_stats.html', context)
    

