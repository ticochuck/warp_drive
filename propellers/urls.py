from django.urls import path

from .views import HomePageView, VehiclePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('vehicles/', VehiclePageView.as_view(), name='vehicles'),
    path('engines/', VehiclePageView.as_view(), name='engines'),
]
