import csv

from django.shortcuts import render
from propellers.models import Vehicle

from .forms import CsvModelForm
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

    return render(request, 'csvs/upload.html', {'form': form})

