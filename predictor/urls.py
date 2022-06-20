from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('predict/', predictor, name="predict"),
    path('result/<int:pk>',result, name="result"),
    path('diabetesbasic/', diabetesbasic, name='diabetesbasic'),
    path('diabetesbasicresult/<int:pk>', diabetesbasicpred, name='diabetesbasicpred'),
    path('basicresult_pdf/<int:pk>', result_diabetes_basic_pdf, name='diabetesbasic_pdf'),
    path('result_pdf/<int:pk>',result_pdf, name="result_pdf"),
]
