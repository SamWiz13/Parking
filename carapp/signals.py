from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from datetime import timedelta
from carapp.models import Order,Place
from django import forms
from django.core.exceptions import ValidationError 

@receiver(post_save, sender=Order)
def create_order(sender, instance, created, **kwargs):
    if created:
        if  instance.place.is_empty:
            raise ValidationError('You can only create an order for an empty place.')
        else:
            instance.place.is_empty = False
            instance.place.save()

@receiver(pre_save, sender=Order)
def update_order(sender, instance=None, **kwargs):
    if instance.id:
        if instance.status == 'exit':
            delta = (timezone.now() - instance.order_date).total_seconds()
            instance.amount = delta * instance.place.pl_amount
    


@receiver(pre_save, sender=Place)
def create_place(sender, instance=None, **kwargs):
    if not instance.id:
        new_places = [Place(building=instance.building, floor=instance.floor, pl_amount=instance.pl_amount, number=i+1) for i in range(instance.number-1)]
        Place.objects.bulk_create(new_places)

        