from re import template
from django.contrib.auth import views as auth_views
from .views import UserRegisterView
from django.urls import path

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name="logout")
    
]
