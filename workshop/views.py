from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import WorkshopProfileForm
from .models import WorkshopProfile


@login_required
def workshop_delete(request, id):
    queryset = WorkshopProfile.objects.filter(author=request.user)
    workshop = get_object_or_404(queryset, pk=id)
    context = {'workshop': workshop}

    if request.method == 'GET':
        return render(request, 'workshop/workshop_delete.html', context)
    elif request.method == 'POST':
        workshop.delete()
        messages.success(request, 'Sklep zostal usuniety pomyslnie.')
        return redirect(workshop_list)

@login_required
def workshop_edit(request, id):
    queryset = WorkshopProfile.objects.filter(author=request.user)
    workshop = get_object_or_404(queryset, id=id)
    context = {'form': WorkshopProfileForm(instance=workshop), 'id': id}
    form = WorkshopProfileForm(request.POST, instance=workshop)

    if request.method == 'GET':
        return render(request, 'workshop/workshop_edit.html', context)

    elif request.method == 'POST':
        if form.is_valid():
            workshop = form.save(commit=False)
            workshop.user = request.user
            workshop.save()
            messages.success(request, 'Sklep został zaktualizowany pomyślnie.')
            return redirect('workshop_list')
        else:
            messages.error(request, 'Popraw następujące błędy:')
            return render(request, 'workshop/workshop_create.html', {'form': form})


@login_required
def workshop_create(request):
    context = {'form': WorkshopProfileForm()}
    form = WorkshopProfileForm(request.POST, request.FILES)

    if request.method == 'GET':
        return render(request, 'workshop/workshop_create.html', context)
    elif request.method == 'POST':
        if form.is_valid():
            workshop = form.save(commit=False)
            workshop.user = request.user
            workshop.save()
            messages.success(request, 'Sklep został utworzony pomyślnie.')
            return redirect('workshop_list')
        else:
            messages.error(request, 'Popraw następujące błędy:')
            return render(request, 'workshop/workshop_create.html', {'form': form})



@login_required
def workshop_list(request):
    workshops = WorkshopProfile.objects.filter(user=request.user)
    return render(request, 'workshop/workshop_list.html', {'workshops': workshops})