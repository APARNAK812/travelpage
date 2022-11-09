from django.test import TestCase

# Create your tests here.


def blog(request):
    return render(request,'user/blog.html')
    
def contact(request):
    return render(request,'user/contact.html')    

def home(request):
    return render(request,'user/home.html')

def login(request):
    return render(request,'user/login.html')  

def membership(request):
    return render(request,'user/membership.html')

def packages(request):
    return render(request,'user/packages.html')