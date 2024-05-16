from django.shortcuts import render

def normal(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')