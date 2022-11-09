from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'user/about.html')

def contact(request):
    return render(request,'user/contact.html')

def home(request):
    return render(request,'user/home.html')

def thingstodo(request):
    return render(request,'user/thingstodo.html')

def membership(request):
    return render(request,'user/membership.html')

def packages(request):
    return render(request,'user/packages.html')
