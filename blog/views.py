from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

# Create your views here.
