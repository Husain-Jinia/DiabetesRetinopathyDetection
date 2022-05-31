from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from user.forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url= reverse_lazy('login')