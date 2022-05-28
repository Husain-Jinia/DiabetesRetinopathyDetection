from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('predict/', predictor, name="predict"),
    path('result/<int:pk>',result, name="result"),
    path('diabetesbasic/', diabetesbasic, name='diabetesbasic'),
    path('diabetesbasicresult', diabetesbasicpred, name='diabetesbasicpred'),
    path('result_pdf/<int:pk>',result_pdf, name="result_pdf"),
]
