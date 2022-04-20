from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def home_view(request,*args, **kwargs):
    context={
        "welcome": "welcome to Microtails!"
    }
    return render(request, "home.html", context)
def about_view(request,*args, **kwargs):
    return render(request, "about.html", {})

def login_view(request,*args, **kwargs):
    return render(request, "login.html", {} )

def register_view(request,*args, **kwargs):
    return render(request, "register.html", {} )

def write_view(request,*args, **kwargs):
    return render(request, "write.html", {} )

def read_view(request,*args, **kwargs):
    return render(request, "read.html", {} )

def faq_view(request, *args, **kwargs):
    return render (request, "faq.html", {})


    
