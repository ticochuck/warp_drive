from django.urls import path

from .views import EnginePageView, HomePageView, VehiclePageView, PropellerPageView, search
from csvs.views import upload_file_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload', upload_file_view, name='upload'),
    path('search/', search, name='search'),
    path('vehicles/', VehiclePageView.as_view(), name='vehicles'),
    path('engines/', EnginePageView.as_view(), name='engines'),
    path('propellers/', PropellerPageView.as_view(), name='propellers')
]
