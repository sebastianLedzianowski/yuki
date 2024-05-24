# repairs/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Repair
from .forms import RepairForm

@login_required
def repair_list(request):
    repairs = Repair.objects.filter(car__user=request.user)
    return render(request, 'repairs/repair_list.html', {'repairs': repairs})

@login_required
def repair_detail(request, repair_id):
    repair = Repair.objects.get(id=repair_id, car__user=request.user)
    return render(request, 'repairs/repair_detail.html', {'repair': repair})

@login_required
def repair_create(request):
    if request.method == 'POST':
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('repair_list')
    else:
        form = RepairForm()
    return render(request, 'repairs/repair_form.html', {'form': form})
