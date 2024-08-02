from django import forms
from django.forms import ModelForm
from carapp.models import Building, Place, Vehicle, Order
from .models import Place
from django.db.models import Count

class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['user', 'building_name', 'location', 'about']

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['building', 'number', 'floor', 'pl_amount', 'is_empty']

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['owner', 'car_type', 'car_number']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['vehicle', 'building', 'place', 'order_date', 'exit_time', 'amount']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['building'].queryset = Place.objects.all()
        
    def get_places_with_one_building():
        return Place.objects.values('building').annotate(building_count=Count('place')).filter(building_count=0)

    
