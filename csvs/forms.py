from crispy_forms.layout import Field
from django import forms

from .models import Csv


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)
        labels = {'Import CSV File here'}
