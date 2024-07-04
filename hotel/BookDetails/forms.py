from django import forms
from .models import BookingField
from django.forms.widgets import DateInput
from datetime import datetime, timedelta

class BookingForm(forms.ModelForm):
    checkin = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    checkout = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    customer = forms.CharField(required=False)
    class Meta:
        model = BookingField
        fields = [
            'checkin', 'checkout','bed'
        ]
        widgets = {
            'bed': forms.Select(attrs={'class': 'form-control'}),
            'adults': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'children': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }
        labels = {
            'bed': 'Bed Type',
            'adults': 'Number of Adults',
            'children': 'Number of Children',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['checkin'].initial = datetime.now().date() + timedelta(days=0)
        self.fields['checkout'].initial = datetime.now().date() + timedelta(days=1)
        
