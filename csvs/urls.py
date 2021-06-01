from django.urls import path

from .views import upload_vehicles, upload_engines, upload_propellers

app_name='csvs'

urlpatterns = [
    path('', upload_vehicles, name='upload_vehicles'),
    path('upload_propellers/', upload_propellers, name='upload_propellers'),
    path('upload_engines/', upload_engines, name='upload_engines'),
    path('upload_vehicles/', upload_vehicles, name='upload_vehicles'),
]

