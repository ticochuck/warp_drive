from django.urls import path

from .views import upload_file_view, upload_propellers

app_name='csvs'

urlpatterns = [
    path('', upload_file_view, name='upload'),
    path('upload_propellers/', upload_file_view, name='upload'),
]
