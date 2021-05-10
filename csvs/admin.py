from django.contrib import admin

from .models import Csv


@admin.register(Csv)
class CsvAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'uploaded_time')
