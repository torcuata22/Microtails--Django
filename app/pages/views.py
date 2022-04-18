from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    return HttpResponse("<h1> Welcome to Microtales!</h1> <br> Would you like to register or login?")


def about_view(request,*args, **kwargs):
    return HttpResponse("<h1> What is Microtales?</h1>")

def login_view(request,*args, **kwargs):
    return HttpResponse("<h1> Login to your account</h1>")

def register_view(request,*args, **kwargs):
    return HttpResponse("<h1> First time here? Register for a free account</h1>")

def write_view(request,*args, **kwargs):
    return HttpResponse("<h1> Start creating</h1>")

def read_view(request,*args, **kwargs):
    return HttpResponse("<h1> These are today's featured tales</h1>")

