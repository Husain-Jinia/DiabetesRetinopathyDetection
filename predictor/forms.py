
from django import forms
from matplotlib import widgets
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset,Field, Div,Row,Column

# class PredictionForm(forms.ModelForm):

#     class Meta:
#         model = DiabetesData
#         fields= ['name', 'pregnancies', 'glucose', 'blood_pressure',  'skin_thickness', 'insulin', 'BMI', 'DPF', 'age']
#         widgets={
#             'name' : forms.TextInput(attrs={'class':'form-control py-2'}),
#             'pregnancies': forms.TextInput(attrs={'class':'form-control py-2'}),
#             'glucose' : forms.TextInput(attrs={'class':'form-control py-2'}),
#             'blood_pressure' : forms.TextInput(attrs={'class':'form-control py-2'}),
#             'skin_thickness' : forms.TextInput(attrs={'class':'form-control py-2'}),
#             'insulin' : forms.TextInput(attrs={'class':'form-control py-2'}),
#             'BMI' : forms.TextInput(attrs={'class':'form-control py-2'}),
#             'DPF' : forms.TextInput(attrs={'class':'form-control py-2'}),
#             'age' : forms.TextInput(attrs={'class':'form-control py-2'})
#         }
#         labels = {
#             'name': ('Enter your name'),
#         }


class DiabetesbasicPredictionForm(forms.ModelForm):

    YES = 1
    NO = 0
   
    STATUS_CHOICES = (
        (YES, 'yes'),
        (NO, 'no')
    )

    MALE = 0
    FEMALE = 1

    GENDER = {
        (MALE,'male'),
        (FEMALE,'female')
    }


    HighBP = forms.ChoiceField(required=False,choices= STATUS_CHOICES, label="Do you have high blood pressure?") 
    smoker= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you smoke frequently")
    heartDiseaseorAttack= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Have you ever had a heart attack")
    stroke= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Have you ever had a stroke?")
    fruits= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you eat fruits?")
    physActivity= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Are you physically active?")
    veggies= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you eat vegetables?")
    hvyAlcoholConsump= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you consume large amounts of alcohol?")
    anyHealthCare= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Any healthcare?")
    NoDocCost= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you actively visit a doctor?")
    diffWalking= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you have difficulty walking?")
    sex= forms.ChoiceField(required=False,choices= GENDER , label="Sex")
    BMI= forms.IntegerField(required=False, label="What is your body mass index?")
    HighChol= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you have high Cholestrol?")
    HighBP= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you have high blood pressure?")
    CholCheck= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you have cholestrol?")
    age= forms.IntegerField(required=True, label="Enter your age", error_messages={'required': 'Please enter your age'})
    class Meta:
        model = Diabetesbasic
        fields = ['HighBP','CholCheck','HighChol','smoker','heartDiseaseorAttack','stroke','fruits','physActivity','veggies','hvyAlcoholConsump','anyHealthCare','NoDocCost','diffWalking','sex','BMI','age']
    
        # labels={
        # 'smoker' : 'Are you a smoker?',
        # 'heartDiseaseorAttack' : 'Have you ever had a heart disease or attack?',
        # 'stroke' : 'Have you ever had a stroke?',
        # 'fruits' : 'Do you eat fruits?',
        # 'physcAtivity' : 'Physical activity?',
        # 'veggies' : 'Do you eat vegetables?',
        # 'hvyAlcoholConsump' : 'Do you consume large amount of liqour/alcohol?',
        # 'anyHealthCare' : 'Any health care?',
        # 'NoDocCost' : 'No doctor cost',
        # 'diffWalking' : 'Do you have difficulty walking?',
        # 'sex' : 'Sex',
        # 'BMI' : 'Enter your Body mass index',
        # 'age' : 'Enter your age?',
        # 'HighBP':'Do you have high blood pressure?',
        # 'CholCheck':'Do you have Cholestrol?',
        # 'HighChol':'Do you have high Cholestrol?',
        # }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


# class HeartDiseasebasicPredictionForm(forms.ModelForm):

#     YES = 1
#     NO = 0
   
#     STATUS_CHOICES = (
#         (YES, 'yes'),
#         (NO, 'no')
#     )

#     MALE = 0
#     FEMALE = 1

#     GENDER = {
#         (MALE,'male'),
#         (FEMALE,'female')
#     }

#     diabetes = forms.ChoiceField(required=False,choices= STATUS_CHOICES, label="Do you have Diabetes?") 
#     HighBP = forms.ChoiceField(required=False,choices= STATUS_CHOICES, label="Do you have high blood pressure?") 
#     smoker= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you smoke frequently")
#     heartDiseaseorAttack= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Have you ever had a heart attack")
#     stroke= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Have you ever had a stroke?")
#     fruits= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you eat fruits?")
#     veggies= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you eat vegetables?")
#     hvyAlcoholConsump= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you consume large amounts of alcohol?")
#     anyHealthCare= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Any healthcare?")
#     NoDocCost= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you actively visit a doctor?")
#     diffWalking= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you have difficulty walking?")
#     sex= forms.ChoiceField(required=False,choices= GENDER , label="Sex")
#     BMI= forms.IntegerField(required=False, label="What is your body mass index?")
#     HighChol= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you have high Cholestrol?")
#     HighBP= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you have high blood pressure?")
#     CholCheck= forms.ChoiceField(required=False,choices= STATUS_CHOICES , label="Do you have cholestrol?")
#     age= forms.IntegerField(required=True, label="Enter your age", error_messages={'required': 'Please enter your age'})
#     class Meta:
#         model = Diabetesbasic
#         fields = ['Diabetes','HighBP','CholCheck','HighChol','smoker','heartDiseaseorAttack','stroke','fruits','veggies','hvyAlcoholConsump','anyHealthCare','NoDocCost','diffWalking','sex','BMI','age']


#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)