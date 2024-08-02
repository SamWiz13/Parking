from django.urls import path
from .views import (
    BuildingListCreateView, BuildingRetrieveUpdateDestroyView,
    PlaceListCreateView, PlaceRetrieveUpdateDestroyView,
    VehicleListCreateView, VehicleRetrieveUpdateDestroyView,
    OrderListCreateView, OrderRetrieveUpdateDestroyView
)

urlpatterns = [
    path('buildings/', BuildingListCreateView.as_view(), name='building-list-create'),
    path('buildings/<int:pk>/', BuildingRetrieveUpdateDestroyView.as_view(), name='building-retrieve-update-destroy'),
    path('places/', PlaceListCreateView.as_view(), name='place-list-create'),
    path('places/<int:pk>/', PlaceRetrieveUpdateDestroyView.as_view(), name='place-retrieve-update-destroy'),
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('vehicles/<int:pk>/', VehicleRetrieveUpdateDestroyView.as_view(), name='vehicle-retrieve-update-destroy'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),
]