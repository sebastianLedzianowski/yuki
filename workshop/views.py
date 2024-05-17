from django.shortcuts import render


def home(request):
    return render(request, 'workshop/home.html',)



def about(request):
    return render(request, 'workshop/about.html')
