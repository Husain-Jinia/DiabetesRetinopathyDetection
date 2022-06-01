from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiabetesData(models.Model):
    name = models.CharField(max_length=256,default="")
    pregnancies = models.CharField(max_length=256, default="")
    glucose = models.CharField(max_length=256, default="")
    blood_pressure = models.CharField(max_length=256, default="")
    skin_thickness = models.CharField(max_length=256, default="")
    insulin = models.CharField(max_length=256, default="")
    BMI = models.CharField(max_length=256, default="")
    DPF = models.CharField(max_length=256, default="")
    age = models.CharField(max_length=256, default="")
    result=models.CharField(max_length=256,default="NEGATIVE")

    def __str__(self):
        return self.name

# TODO : Create diabetes-bsc db model (b-boolean value)
# Smoker-b,	Stroke-b,	HeartDiseaseorAttack-b,	PhysActivity-b,	Fruits-b,	
# Veggies-b,	HvyAlcoholConsump-b,	AnyHealthcare-b,	NoDocbcCost-b,	
# GenHlth (1-5 scale),	DiffWalk-b,	Sex-b,	Age

# TODO (#2) : Replace IntegerField with IntegerChoices field

class DiabetesBasic(models.Model):
    smoker = models.IntegerField(max_length=1,default=0)
    heartDiseaseorAttack = models.IntegerField(max_length=1,default=0)
    stroke = models.IntegerField(max_length=1,default=0)
    fruits = models.IntegerField(max_length=1,default=0)
    physActivity = models.IntegerField(max_length=1,default=0)
    veggies = models.IntegerField(max_length=1,default=0)
    hvyAlcoholConsump = models.IntegerField(max_length=1,default=0)
    anyHealthCare = models.IntegerField(max_length=1,default=0)
    NoDocCost = models.IntegerField(max_length=1,default=0)
    diffWalking = models.IntegerField(max_length=1,default=0)
    sex =models.IntegerField(max_length=1,default=0)
    genHealth = models.IntegerField(max_length=1, default=0)
    age = models.IntegerField(max_length=3,default=0)


# wfwwrqfc