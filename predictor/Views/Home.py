from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic import  CreateView

def home(request):
    return render(request, 'home.html')