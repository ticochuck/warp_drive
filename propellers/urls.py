from django.urls import path

from csvs.views import upload_file_view, upload_propellers

from .views import (EnginePageView, HomePageView, PropellerPageView,
                    VehiclePageView, database_page, overall_stats, search, home)

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_file_view, name='upload'),
    path('overall_stats/', overall_stats, name='overall_stats'),
    path('upload_propellers/', upload_propellers, name='upload_propellers'),
    path('search/', search, name='search'),
    path('results/', search, name='results'),
    path('databases/', database_page, name='databases'),
    path('vehicles/', VehiclePageView.as_view(), name='vehicles'),
    path('engines/', EnginePageView.as_view(), name='engines'),
    path('propellers/', PropellerPageView.as_view(), name='propellers'),
]
