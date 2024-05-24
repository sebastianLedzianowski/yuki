# cars/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Car
from .forms import CarForm

@login_required
def car_list(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/car_list.html', {'cars': cars})

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id, user=request.user)
    return render(request, 'cars/car_detail.html', {'car': car})

@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})
