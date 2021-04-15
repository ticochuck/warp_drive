from django.urls import path

from .views import EnginePageView, HomePageView, VehiclePageView, PropellerPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('vehicles/', VehiclePageView.as_view(), name='vehicles'),
    path('engines/', EnginePageView.as_view(), name='engines'),
    path('propellers/', PropellerPageView.as_view(), name='propellers')
]
