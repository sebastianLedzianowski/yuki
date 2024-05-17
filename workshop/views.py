from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ShopProfileForm
from .models import ShopProfile

@login_required
def workshop_create(request):
    if request.method == 'POST':
        form = ShopProfileForm(request.POST, request.FILES)
        if form.is_valid():
            workshop = form.save(commit=False)
            workshop.user = request.user
            workshop.save()
            messages.success(request, 'Sklep został utworzony pomyślnie.')
            return redirect('workshop_list')
        else:
            messages.error(request, 'Popraw następujące błędy:')
            return render(request, 'workshop/workshop_create.html', {'form': form})
    else:
        context = {'form': ShopProfileForm()}
        return render(request, 'workshop/workshop_create.html', context)


@login_required
def workshop_list(request):
    shops = ShopProfile.objects.filter(user=request.user)
    return render(request, 'workshop/workshop_list.html', {'shops': shops})
