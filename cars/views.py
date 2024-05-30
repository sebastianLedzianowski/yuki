from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Car
from .forms import CarForm
from django.views.generic.list import ListView

class CarList(ListView):
    model = Car
    context_object_name = 'cars'


