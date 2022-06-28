import imp
from django.contrib import admin
from django.urls import path, include
from predictor.Views.Disease.Diabetes import *
from predictor.Views.Disease.HeartDisease import *
from predictor.Views.Home import home


urlpatterns = [
    path('',home,name='home'),
    path('diabetesbasic/', diabetesbasic, name='diabetesbasic'),
    path('diabetesbasicresult/<int:pk>', diabetesbasicpred, name='diabetesbasicpred'),
    path('basicresult_pdf/<int:pk>', result_diabetes_basic_pdf, name='diabetesbasic_pdf'),
    path('heartdisease/', heartdisease, name='heartdisease' ),
    path('heartdiseaseresult/<int:pk>', heartdiseasepred, name="heartdiseaseresult"),
    path('heartdisease_pdf/', result_heartdisease_pdf, name='heartdisease_pdf' ),
]

