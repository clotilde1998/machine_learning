from dataclasses import fields
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'age', 'sexe', 'cas']
