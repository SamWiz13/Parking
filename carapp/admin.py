from django.contrib import admin
from .models import Building, Place, Vehicle, Order


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_name', 'location', 'about')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('building', 'number', 'floor', 'pl_amount', 'is_empty')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'car_type', 'car_number')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'building', 'place', 'order_date', 'exit_time', 'amount')

admin.site.register(Building, BuildingAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Order, OrderAdmin)