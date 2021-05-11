import csv

from django.shortcuts import render

from propellers.models import Engine, Propeller, Vehicle

from .forms import CsvModelForm, PropellerCsvModelForm
from .models import Csv


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)

        #open and read csv file
        with open(obj.file_name.path, 'r') as f:

            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    # convert row to str
                    # row = "".join(row)
                    # replace , with space
                    # row = row.replace(",", " ")
                    # split and make it a list
                    # row = row.split()
                    
                    # print(row)
                    # print(type(row))
                    
                    Vehicle.objects.create(
                        name = row[1],
                        manufacturer = row[2],
                        model = row[3],
                        vehicle_type = row[4],
                        prop_orientation = row[5],
                        notes = row[6],
                    )
                    
            obj.activated = True
            obj.save()

    return render(request, 'propellers/upload.html', {'form': form})


def upload_propellers(request):
    form = PropellerCsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = PropellerCsvModelForm()
        obj = Csv.objects.get(activated=False)

        #open and read csv file
        with open(obj.file_name.path, 'r') as f:

            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    Propeller.objects.create(
                        name = row[0],
                        product_id = row[1],
                        old_Serial = row[2],
                        new_Serial = row[3],
                        hub_Serial = row[4],
                        status = row[5],
                        do_not_import = row[6],
                        hub_model = row[7],
                        blade_count = row[8],
                        blade_model = row[9],
                        bld_dia = row[10],
                        taper = row[11],
                        rotation = row[12],
                        taper_specs = row[13],
                        nickel_LE = row[14],
                        tip_color = row[15],
                        weight_start = row[16],
                        weight_end = row[17],
                        weight_vert = row[18],
                        weight_taperbefore = row[19],
                        weight_taperafter = row[20],
                        tracking = row[21],
                        bld_notes = row[22],
                        pinned_collars = row[23],
                        customer_id = row[24],
                        customer_notes = row[25],
                        vehicle_id = row[26],
                        vehicle_notes = row[27],
                        engine_id = row[28],
                        engine_notes = row[29],
                        bolt_pattern = row[30],
                        bolt_pattern_notes_new_field = row[31],
                        reduction_ratio_rename_to_red_drive_name = row[32],
                        reduction_style = row[33],
                        update_1_date = row[34],
                        update_1 = row[35],
                        update_2_date = row[36],
                        update_2 = row[37],
                        update_3_date = row[38],
                        update_3 = row[39],
                        update_4_date = row[40],
                        update_4 = row[41],
                        update_5_Date = row[42],
                        update_5 = row[43],
                        x_studio_ship_date = row[44],
                        old_notes = row[45],
                        old_bldspecs = row[46],
                        old_bldnum = row[47],
                        old_bldtype = row[48],
                        old_hub = row[49],
                    )
                    
            obj.activated = True
            obj.save()

    return render(request, 'propellers/upload.html', {'form': form})
