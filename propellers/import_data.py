import csv

from import_export import resources

from .models import Vehicle


class VehicleResource(resources.ModelResource):
    class meta:
        model = Vehicle


# with open('../data/Vehicles_test_data.csv') as vehicle_test:
#     csv_reader = csv.reader(vehicle_test, delimiter=',')
#     for row in vehicle_test:
#         print(row)
#         new_vehicle = Vehicle(name=new_vehicle['name'])
