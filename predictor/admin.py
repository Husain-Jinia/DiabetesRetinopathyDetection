from django.contrib import admin
from .models import DiabetesData, DiabetesBasic

# Register your models here.
admin.site.register(DiabetesData)
admin.site.register(DiabetesBasic)