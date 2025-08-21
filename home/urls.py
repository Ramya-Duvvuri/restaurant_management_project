from django.urls import path
from .views import *

urlpatterns = [
    path('reservations/'views.reservations_view , name ='reservations'),
]