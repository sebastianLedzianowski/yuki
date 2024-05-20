from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Rejestracja zakonczona sukcesem.')
            login(request, user)
            return redirect('workshop_list')
        else:
            return render(request, 'users/register.html', {'form': form})


def sing_in(request):
    form_get = LoginForm()
    form_post = LoginForm(request.POST)

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('posts')

        return render(request, 'users/login.html', {'form': form_get})

    elif request.method == 'POST':
        if form_post.is_valid():
            username = form_post.cleaned_data['username']
            password = form_post.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Cześć {username.title()}, witamy z powrotem!')
                return redirect('workshop_list')

        messages.error(request, f'Nieprawidłowy login lub hasło.')
        return render(request, 'users/login.html', {'form': form_get})


def sign_out(request):
    logout(request)
    messages.success(request, f'Zostałeś wylogowany.')
    return redirect('login')