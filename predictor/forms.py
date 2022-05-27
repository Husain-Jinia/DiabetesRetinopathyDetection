from django import forms
from .models import *

class PredictionForm(forms.ModelForm):

    class Meta:
        model = DiabetesData
        fields= ['name', 'pregnancies', 'glucose', 'blood_pressure',  'skin_thickness', 'insulin', 'BMI', 'DPF', 'age']
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'pregnancies': forms.TextInput(attrs={'class':'form-control py-2'}),
            'glucose' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'blood_pressure' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'skin_thickness' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'insulin' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'BMI' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'DPF' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'age' : forms.TextInput(attrs={'class':'form-control py-2'})
        }


class DiabetesbasicPredictionForm(forms.ModelForm):
    
    class Meta:
        model = DiabetesBasic
        fields = {'user','smoker','heartDiseaseorAttack','stroke','fruits','physActivity','veggies','hvyAlcoholConsumpany','HealthCare','NoDocCost','diffWalking','sex','genHealth','age'}
        widgets={
        'user': forms.TextInput(attrs={'class':'form-control py-2'}),
        'smoker' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'heartDiseaseorAttack' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'stroke' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'fruits' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'physActivity' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'veggies' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'hvyAlcoholConsumpany' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'HealthCare' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'NoDocCost' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'diffWalking' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'sex' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'genHealth' : forms.TextInput(attrs={'class':'form-control py-2'}),
        'age' : forms.TextInput(attrs={'class':'form-control py-2'})
        }