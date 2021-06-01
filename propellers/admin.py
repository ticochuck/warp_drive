from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import Engine, Propeller, Vehicle


@admin.register(Vehicle)
class VehicleAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'manufacturer', 'model', 'vehicle_type', 'prop_orientation')


@admin.register(Engine)
class EngineAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'manufacturer', 'model', 'notes')


@admin.register(Propeller)
class PropellerAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'vehicle_id', 'engine_id')
