from django.shortcuts import render

def cards(request):
    return render(request, 'index.html')