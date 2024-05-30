from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import WorkshopForm
from .models import Workshop

@login_required
def workshop_delete(request, id):
    queryset = Workshop.objects.filter(owner=request.user)
    workshop = get_object_or_404(queryset, pk=id)
    context = {'workshop': workshop}

    if request.method == 'GET':
        return render(request, 'workshop/workshop_delete.html', context)
    elif request.method == 'POST':
        workshop.delete()
        messages.success(request, 'Sklep został usunięty pomyślnie.')
        return redirect('workshop_list')

@login_required
def workshop_edit(request, id):
    queryset = Workshop.objects.filter(owner=request.user)
    workshop = get_object_or_404(queryset, id=id)

    if request.method == 'GET':
        form = WorkshopForm(instance=workshop)
        context = {'form': form, 'id': id}
        return render(request, 'workshop/workshop_edit.html', context)

    elif request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES, instance=workshop)
        if form.is_valid():
            workshop = form.save(commit=False)
            workshop.owner = request.user
            workshop.save()
            messages.success(request, 'Sklep został zaktualizowany pomyślnie.')
            return redirect('workshop_list')
        else:
            messages.error(request, 'Popraw następujące błędy:')
            return render(request, 'workshop/workshop_edit.html', {'form': form, 'id': id})

@login_required
def workshop_create(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            workshop = form.save(commit=False)
            workshop.owner = request.user
            workshop.save()
            messages.success(request, 'Sklep został utworzony pomyślnie.')
            return redirect('workshop_list')
        else:
            messages.error(request, 'Popraw następujące błędy:')
            return render(request, 'workshop/workshop_create.html', {'form': form})
    else:
        form = WorkshopForm()
        context = {'form': form}
        return render(request, 'workshop/workshop_create.html', context)

@login_required
def workshop_list(request):
    workshops = Workshop.objects.filter(owner=request.user)
    return render(request, 'workshop/workshop_list.html', {'workshops': workshops})

def home(request):
    return render(request, 'home.html')
