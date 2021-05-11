from django.urls import path

from .views import EnginePageView, HomePageView, VehiclePageView, PropellerPageView, search

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', search, name='search'),
    path('vehicles/', VehiclePageView.as_view(), name='vehicles'),
    path('engines/', EnginePageView.as_view(), name='engines'),
    path('propellers/', PropellerPageView.as_view(), name='propellers')
]
