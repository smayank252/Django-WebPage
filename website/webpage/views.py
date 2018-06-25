from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login, Signup

def home(request):
    return render(request, 'webpage/home.html')

def contact(request):
    return render(request, 'webpage/contact.html')

def login(request):
    form = Login()
    return render(request, 'webpage/login.html',{ 'form': form, })

def profile(request):
    return render (request, 'webpage/profile.html')

def signup(request):
     form = Signup()
     return render(request,'webpage/signup.html',{ 'form':form,})

def mksignup(request) :
    return render(request, 'webpage/mksignup.html')

def mklogin(request) :
    return render(request, 'webpage/mklogin.html')





