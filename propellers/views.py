# import matplotlib

# matplotlib.use('Agg')

import base64
from io import BytesIO

# import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django_pandas.io import read_frame

from .forms import SearchPropeller
from .models import Engine, Propeller, Vehicle
from .plots import get_plot
from .utils import simple_plot


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
            
            # data = data_analysis(results)
            data2 = data_analysis2(results)

            x = [x.engine_id for x in results]
            y = [y.reduction_ratio_rename_to_red_drive_name for y in results]
            chart =  get_plot(x,y)

            
            
        message = 'No results found. Please try searching with different criteria'

        context = {
            'title': 'Results',
            'results': results,
            'message' : message,
            'chart': chart,
            # 'graph': data,
            # 'df': data.to_html()
        }

        return render(request, 'propellers/results.html', context)

    else:
        form = SearchPropeller()

    context = {
        'title': 'Search',
        'form': form,
    }
    
    return render(request, 'propellers/search.html', context)


def data_analysis2(results):

    df = pd.DataFrame(results)
    df = df.head(10)
    print(df)
    # sns.set()

    # print(df.head(10))
    pass

def data_analysis(results):
    
    # create DataFrame
    qs = read_frame(results)
    df = pd.DataFrame(results)
    df['engine_id'] = df['engine_id'].apply(lambda x: x.strftim())
    # get top 5 most common engines
    most_common_engines_names = qs['engine_id'].value_counts()[:10].index.tolist()
    
    most_common_engines_totals = qs['engine_id'].value_counts()[:10].tolist()
    
    most_common_red_drives = qs['reduction_ratio_rename_to_red_drive_name'].value_counts()[:10].tolist()

    data = [most_common_engines_names, most_common_engines_totals, most_common_red_drives]
    
    graph = simple_plot(x=df['engine_id'], y=df['reduction_ratio_rename_to_red_drive_name'])

    return graph


def overall_stats(request):
    qs = Propeller.objects.all().filter(vehicle_id = 'un-Gyro').values()
    data = pd.DataFrame(qs).drop(['id', 'old_Serial', 'new_Serial', 'hub_Serial', 'status', 'product_id', 'do_not_import', 'hub_model', 'taper_specs', 'tip_color', 'weight_start', 'weight_end', 'weight_vert', 'weight_taperbefore', 'weight_taperafter', 'tracking', 'bld_notes', 'pinned_collars', 'customer_notes', 'vehicle_notes', 'engine_notes', 'bolt_pattern_notes_new_field', 'reduction_style', 'update_1_date', 'update_1', 'update_2_date', 'update_2', 'update_3_date', 'update_3', 'update_4_date', 'update_4', 'update_5_Date', 'update_5', 'x_studio_ship_date', 'old_notes', 'old_bldspecs', 'old_bldnum', 'old_bldtype', 'old_hub'], axis=1)
    
    data2 = pd.DataFrame(Propeller.objects.all().filter(vehicle_id = 'un-Gyro').values())
    
    d = data2.groupby('engine_id')['reduction_ratio_rename_to_red_drive_name'].count().sort_values(ascending=False).head(10)
    
    data2 = data2['engine_id'].value_counts().head(10)
       
    ts = Propeller.objects.all().filter(vehicle_id='Messerschmitt ME109')
    # x = [x.engine_id for x in ts]
    
    # y = [y.reduction_ratio_rename_to_red_drive_name for y in ts]
    # plt.title('Engines and Red Rates')
    # plt.plot(x,y)
    # plt.xticks(rotation=45)
    # plt.xlabel('Engines')
    # plt.ylabel('Reduction Rates')
    # plt.tight_layout()
    
    # buf = BytesIO()
    # plt.savefig(buf, format='png', dpi=100)
    # image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    # buf.close()

    context = {
        'title': 'Stats',
        'df': data.to_html(),
        'data2': data2,
        'd': d,
        # 'chart': image_base64
    }

    return render(request, 'propellers/overall_stats.html', context)
    

