
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset,Field, Div,Row,Column

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
        model = Diabetesbasic
        fields = {'HighBP','CholCheck','HighChol','smoker','heartDiseaseorAttack','stroke','fruits','physActivity','veggies','hvyAlcoholConsump','anyHealthCare','NoDocCost','diffWalking','sex','BMI','age'}
        # widgets={
        # 'smoker' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'heartDiseaseorAttack' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'stroke' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'fruits' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'physcAtivity' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'veggies' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'hvyAlcoholConsump' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'anyHealthCare' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'NoDocCost' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'diffWalking' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'sex' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'BMI' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'age' : forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'HighBP':forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'CholCheck':forms.IntegerField(attrs={'class':'form-control py-2'}),
        # 'HighChol':forms.IntegerField(attrs={'class':'form-control py-2'}),
        # }

        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column('smoker'),
                    Column('heartDiseaseorAttack')
                )

            )
            