from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


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


class Diabetesbasic(models.Model):
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


    smoker = models.IntegerField(default=0, choices = STATUS_CHOICES )
    heartDiseaseorAttack = models.IntegerField(default=0, choices = STATUS_CHOICES)
    stroke = models.IntegerField(default=0, choices = STATUS_CHOICES)
    fruits = models.IntegerField(default=0, choices = STATUS_CHOICES)
    physActivity = models.IntegerField(default=0, choices = STATUS_CHOICES)
    veggies = models.IntegerField(default=0, choices = STATUS_CHOICES)
    hvyAlcoholConsump = models.IntegerField(default=0, choices = STATUS_CHOICES)
    anyHealthCare = models.IntegerField(default=0, choices = STATUS_CHOICES)
    NoDocCost = models.IntegerField(default=0, choices = STATUS_CHOICES)
    diffWalking = models.IntegerField(default=0, choices = STATUS_CHOICES)
    sex =models.IntegerField(default=0, choices = GENDER)
    BMI = models.IntegerField(default=0)
    HighChol = models.IntegerField(default=0, choices = STATUS_CHOICES)
    HighBP = models.IntegerField(default=0, choices = STATUS_CHOICES)
    CholCheck = models.IntegerField(default=0, choices = STATUS_CHOICES)
    age = models.IntegerField(default=0) 

#Highbp highchol cholcheck BMI smoker stroke diabetes fruits vegetables heavyalcoholconsump healthcare NoDocCost DiffWalk sex age

class HeartDisease(models.Model):
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


    smoker = models.IntegerField(default=0, choices = STATUS_CHOICES )
    heartDiseaseorAttack = models.IntegerField(default=0, choices = STATUS_CHOICES)
    stroke = models.IntegerField(default=0, choices = STATUS_CHOICES)
    fruits = models.IntegerField(default=0, choices = STATUS_CHOICES)
    diabetes = models.IntegerField(default=0, choices = STATUS_CHOICES)
    veggies = models.IntegerField(default=0, choices = STATUS_CHOICES)
    hvyAlcoholConsump = models.IntegerField(default=0, choices = STATUS_CHOICES)
    anyHealthCare = models.IntegerField(default=0, choices = STATUS_CHOICES)
    NoDocCost = models.IntegerField(default=0, choices = STATUS_CHOICES)
    diffWalking = models.IntegerField(default=0, choices = STATUS_CHOICES)
    sex =models.IntegerField(default=0, choices = GENDER)
    BMI = models.IntegerField(default=0)
    HighChol = models.IntegerField(default=0, choices = STATUS_CHOICES)
    HighBP = models.IntegerField(default=0, choices = STATUS_CHOICES)
    CholCheck = models.IntegerField(default=0, choices = STATUS_CHOICES)
    age = models.IntegerField(default=0) 


    