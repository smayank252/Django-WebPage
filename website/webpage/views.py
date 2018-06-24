from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'webpage/home.html')

def client(request):
    return render(request, 'webpage/maya.html')
