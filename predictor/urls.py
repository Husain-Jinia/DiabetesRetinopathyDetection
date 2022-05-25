from django.contrib import admin
from django.urls import path, include
from .views import predictor,result, result_pdf, suggestion, home


urlpatterns = [
    path('',home,name='home'),
    path('predict/', predictor, name="predict"),
    path('result/<int:pk>',result, name="result"),
    path('result_pdf/<int:pk>',result_pdf, name="result_pdf"),
]
