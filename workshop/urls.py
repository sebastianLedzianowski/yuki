from django.urls import path
from . import views

urlpatterns = [
    path('', views.workshop_list, name='workshop_list'),
    path('workshop/create', views.workshop_create, name='workshop_create'),
]