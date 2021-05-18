from crispy_forms.layout import Field
from django import forms

from .models import Csv


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)
        labels = {'file_name': 'Import File '}
        help_texts = {'file_name': 'Must be a CSV file'}


class PropellerCsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)
        labels = {'file_name': 'Import File'}
        help_texts = {'file_name': 'Must be a CSV file'}
