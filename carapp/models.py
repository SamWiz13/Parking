from typing import Iterable
from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Building(models.Model):
    user = models.ForeignKey(CustomUser, on_delete =models.CASCADE)
    building_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100,null=True, blank=True)
    about = models.TextField(max_length=200,null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.building_name} -  {self.location} - {self.about}'


class Place(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    number = models.IntegerField()
    floor = models.IntegerField()
    pl_amount = models.IntegerField(default=5)
    is_empty = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.building.building_name} - {self.number} - {self.floor} - {self.pl_amount} - {self.is_empty}'


class Vehicle(models.Model):
    owner =models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car_type =models.CharField(max_length=20)
    car_number =models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.owner} - {self.car_type} - {self.car_number}'

# def validate_place(value):
#     p = Place.objects.filter(id=value).first()
#     if not p.is_empty:
#         raise ValidationError('Place is not empty')

class Order(models.Model):
    choice_status = (
        ('enter', 'enter'),
        ('exit', 'exit')
    )
    status = models.CharField(max_length=10,choices=choice_status, default='enter')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    building = models.ForeignKey(Building,null=True,blank=True, on_delete = models.SET_NULL)
    place = models.ForeignKey(Place,null=True,blank=True, on_delete = models.SET_NULL,related_name='orders') 
    order_date = models.DateField(auto_now_add=True)
    exit_time = models.DateField(auto_now = True)
    amount = models.PositiveBigIntegerField(null=True, default=0)

    def __str__(self):
        return self.vehicle.car_number
 