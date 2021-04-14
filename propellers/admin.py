from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import Vehicle, Engine

@admin.register(Vehicle)
class VehicleAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'manufacturer', 'model', 'vehicle_type', 'prop_orientation', 'notes')


@admin.register(Engine)
class EngineAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'manufacturer', 'model', 'notes')
