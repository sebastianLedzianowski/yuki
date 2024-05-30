# cars/urls.py
from django.urls import path
from . import views
from .views import CarList

urlpatterns = [
    path('', CarList.as_view(), name='car_list'),
]
