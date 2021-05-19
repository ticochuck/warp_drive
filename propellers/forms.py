from crispy_forms.layout import Field
from django import forms

from .models import Propeller


class SearchPropeller(forms.ModelForm):

    class Meta:
        model = Propeller
        fields = ['vehicle_id', 'engine_id', 'reduction_ratio_rename_to_red_drive_name']
        labels = {
            'vehicle_id': 'Vehicle ID',
            'engine_id': 'Engine ID',
            'reduction_ratio_rename_to_red_drive_name': 'Reduction Drive',
        }
        help_texts = {
            'vehicle_id': 'Vehicle ids containing...',
            'engine_id': 'Engine ids containing...',
            'reduction_ratio_rename_to_red_drive_name': 'Reduction Drives containing...',
        }
