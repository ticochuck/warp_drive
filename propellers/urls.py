from django.urls import path

from csvs.views import upload_engines, upload_propellers, upload_vehicles

from .views import (EnginePageView, PropellerPageView, VehiclePageView,
                    database_page, home, overall_stats, search)

urlpatterns = [
    path('', home, name='home'),
    path('overall_stats/', overall_stats, name='overall_stats'),
    path('search/', search, name='search'),
    path('results/', search, name='results'),
    path('databases/', database_page, name='databases'),
    path('upload_vehicles/', upload_vehicles, name='upload_vehicles'),
    path('upload_propellers/', upload_propellers, name='upload_propellers'),
    path('upload_engines/', upload_engines, name='upload_engines'),
    path('vehicles/', VehiclePageView.as_view(), name='vehicles'),
    path('engines/', EnginePageView.as_view(), name='engines'),
    path('propellers/', PropellerPageView.as_view(), name='propellers'),
]
