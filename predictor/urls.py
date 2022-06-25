import imp
from django.contrib import admin
from django.urls import path, include
from predictor.Views.Disease.Diabetes import *
from predictor.Views.Home import home


urlpatterns = [
    path('',home,name='home'),
    path('diabetesbasic/', diabetesbasic, name='diabetesbasic'),
    path('diabetesbasicresult/<int:pk>', diabetesbasicpred, name='diabetesbasicpred'),
    path('basicresult_pdf/<int:pk>', result_diabetes_basic_pdf, name='diabetesbasic_pdf'),
]

