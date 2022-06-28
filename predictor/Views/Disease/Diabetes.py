# django imports
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic import  CreateView
from predictor.forms import DiabetesbasicPredictionForm
from predictor.models import *
from predictor.Views.Utils.DocSuggestion import suggestion
from predictor.Views.Utils.PDFGenerartion import pdf_generation_utils

# model building
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
import csv
from sklearn.metrics import confusion_matrix
import pickle
import json
import requests

# document generation  
from django.http import FileResponse, QueryDict
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont


def diabetesbasic(request):
    forms_pk = None
    
    form= DiabetesbasicPredictionForm(request.POST )
    
    context = {'form':form }
    if form.is_valid():
        form.save()
        x = form.save()
        forms_pk = x.pk

        return redirect(f'/diabetesbasicresult/'+ str(forms_pk))
    return render(request,'diabetes/diabetesbasicpred.html',context)


def diabetesbasicpred(request,pk):
    pk=int(pk)

    values = Diabetesbasic.objects.get(pk=pk)


    val2 = float(values.smoker)
    val3 = float(values.heartDiseaseorAttack)
    val4 = float(values.stroke)
    val5 = float(values.fruits)
    val6 = float(values.physActivity)
    val7 = float(values.veggies)
    val8 = float(values.hvyAlcoholConsump)
    val9 = float(values.anyHealthCare)
    val10 = float(values.NoDocCost)
    val11 = float(values.diffWalking)
    val12 = float(values.sex)
    val13 = float(values.BMI)
    val15 = float(values.HighBP)
    val16 = float(values.CholCheck)
    val17 = float(values.HighChol)
    val18 = float(values.age)



    loaded_model = pickle.load(open('/home/husain/Projects/IBM-mini-project/models/diabetes_modelbasic.sav', 'rb'))
    # result = loaded_model.score(X_test, Y_test)

    y_pred= loaded_model.predict([[val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val15,val16,val17,val18]])
    print(y_pred)

    result=""
    if y_pred >= [1.]:
        result = "POSITIVE"
        data = suggestion()
        return render(request, 'diabetes/diabetesBasicResult.html',{'result':result,'values':values, 'data':data})
    else:
        result="NEGATIVE"
        return render(request, 'diabetes/diabetesBasicResult.html', {'result':result,'values':values}) 

def result_diabetes_basic_pdf(request,pk):
    buf = io.BytesIO() 
    fileName = 'Diabetes_results.pdf'
    
    documentTitle = 'Diabetes Basic'
    pdf = canvas.Canvas(buf,fileName)
    pdf.setTitle(documentTitle)
    pdf_generation_utils(pdf)
    title = 'Diabetes diagnosis report'
    factors="factors"
    values_text = "Values"

    # HighBP	HighChol	CholCheck	BMI	Smoker	Stroke	HeartDiseaseorAttack	PhysActivity	Fruits	Veggies	HvyAlcoholConsump	AnyHealthcare	NoDocbcCost		DiffWalk	Sex	Age

    patient_data = Diabetesbasic.objects.get(pk=pk)

    pdf.setFillColorRGB(65/256, 108/256, 141/256)
    pdf.rect(0,645,700,35,stroke=0,fill=1)
    pdf.setFillColor(colors.whitesmoke)
    pdf.setFont("Helvetica-BoldOblique", 16)
    title_text = pdf.beginText(30,660)
    title_text.textLine(title)
    pdf.drawText(title_text)

    pdf.setFillColorRGB(27/256, 47/256, 63/256)
    pdf.setFont("Helvetica", 13)

    text0 = pdf.beginText(50,580)
    text1 = pdf.beginText(50,540)
    text2 = pdf.beginText(50,520)
    text3 = pdf.beginText(50,500)
    text4 = pdf.beginText(50,480)
    text5 = pdf.beginText(50,460)
    text6 = pdf.beginText(50,440)
    text7 = pdf.beginText(50,420)
    text8 = pdf.beginText(50,400)
    text9 = pdf.beginText(50,380)
    text10 = pdf.beginText(50,360)
    text11 = pdf.beginText(50,340)
    text12 = pdf.beginText(50,320)
    text13 = pdf.beginText(50,300)
    text14 = pdf.beginText(50,280)
    text15 = pdf.beginText(50,260)
    text16 = pdf.beginText(50,240)
    text17 = pdf.beginText(50,200)

    smoker_text ="smoker"
    heartDiseaseorAttack_text = "Heart disease / Attack"
    stroke_text = "stroke"
    fruits_text = "fruits eaten"
    physActivity_text = "Physical activity"
    veggies_text = "Veggies"
    hvyAlcoholConsump_text = "Heavy Alcohol Consumption"
    anyHealthCare_text = "Any health care"
    NoDocCost_text = "No doctor cost"
    diffWalking_text  = "Diffiulty Walking"
    sex_text = "sex"
    BMI_text = "Body mass index"
    HighChol_text = "High Cholestrol"
    HighBP_text  = "High blood pressure"
    CholCheck_text = "Cholestrol Check"
    age_text = "age"
    result_text = "result"

    smoker = patient_data.smoker
    
    heartDiseaseorAttack = patient_data.heartDiseaseorAttack
    stroke = patient_data.stroke    
    fruits = patient_data.fruits
    physActivity = patient_data.physActivity
    veggies = patient_data.veggies
    hvyAlcoholConsump = patient_data.hvyAlcoholConsump
    anyHealthCare = patient_data.anyHealthCare
    NoDocCost = patient_data.NoDocCost
    diffWalking = patient_data.diffWalking
    sex = patient_data.sex
    BMI = patient_data.BMI
    HighChol = patient_data.HighChol
    HighBP = patient_data.HighBP
    CholCheck = patient_data.CholCheck
    age = patient_data.age
    result="POSITIVE"



    
    v_text0 = pdf.beginText(490,580)
    
    pdf.setLineWidth(1)
    pdf.line(40, 560, 550, 560)
    v_text1 = pdf.beginText(510,540)
    v_text2 = pdf.beginText(510,520)
    v_text3 = pdf.beginText(510,500)
    v_text4 = pdf.beginText(510,480)
    v_text5 = pdf.beginText(510,460)
    v_text6 = pdf.beginText(510,440)
    v_text7 = pdf.beginText(510,420)
    v_text8 = pdf.beginText(510,400)
    v_text9 = pdf.beginText(510,380)
    v_text10 = pdf.beginText(510,360)
    v_text11 = pdf.beginText(510,340)
    v_text12 = pdf.beginText(510,320)
    v_text13 = pdf.beginText(510,300)
    v_text14 = pdf.beginText(510,280)
    v_text15 = pdf.beginText(510,260)
    v_text16 = pdf.beginText(510,240)
    v_text17 = pdf.beginText(480,200)

    v_text0.textLine(values_text)
    pdf.drawText(v_text0)
    v_text1.textLine(str(smoker))
    v_text2.textLine(str(heartDiseaseorAttack))
    v_text3.textLine(str(stroke))
    v_text4.textLine(str(fruits))
    v_text5.textLine(str(physActivity))
    v_text6.textLine(str(veggies))
    v_text7.textLine(str(hvyAlcoholConsump))
    v_text8.textLine(str(anyHealthCare))
    v_text9.textLine(str(NoDocCost))
    v_text10.textLine(str(diffWalking))
    v_text11.textLine(str(sex))
    v_text12.textLine(str(BMI))
    v_text13.textLine(str(HighChol))
    v_text14.textLine(str(HighBP))
    v_text15.textLine(str(CholCheck))
    v_text16.textLine(str(age))
    v_text17.textLine(str(result))

    

    text0.textLine(factors)
    pdf.drawText(text0)
    text1.textLine(smoker_text)
    text2.textLine(heartDiseaseorAttack_text)
    text3.textLine(stroke_text)
    text4.textLine(fruits_text)
    text5.textLine(physActivity_text)
    text6.textLine(veggies_text)
    text7.textLine(hvyAlcoholConsump_text)
    text8.textLine(anyHealthCare_text)
    text9.textLine(NoDocCost_text)
    text10.textLine(diffWalking_text)
    text11.textLine(sex_text)
    text12.textLine(BMI_text)
    text13.textLine(HighChol_text)
    text14.textLine(HighBP_text)
    text15.textLine(CholCheck_text)
    text16.textLine(age_text)
    text17.textLine(result_text)


    pdf.drawText(text1)
    pdf.drawText(text2)
    pdf.drawText(text3)
    pdf.drawText(text4)
    pdf.drawText(text5)
    pdf.drawText(text6)
    pdf.drawText(text7)
    pdf.drawText(text8)
    pdf.drawText(text9)
    pdf.drawText(text10)
    pdf.drawText(text11)
    pdf.drawText(text12)
    pdf.drawText(text13)
    pdf.drawText(text14)
    pdf.drawText(text15)
    pdf.drawText(text16)
    pdf.drawText(text17)

    pdf.drawText(v_text1)
    pdf.drawText(v_text2)
    pdf.drawText(v_text3)
    pdf.drawText(v_text4)
    pdf.drawText(v_text5)
    pdf.drawText(v_text6)
    pdf.drawText(v_text7)
    pdf.drawText(v_text8)
    pdf.drawText(v_text9) 
    pdf.drawText(v_text10)
    pdf.drawText(v_text11)
    pdf.drawText(v_text12) 
    pdf.drawText(v_text13)   
    pdf.drawText(v_text14) 
    pdf.drawText(v_text15) 
    pdf.drawText(v_text16) 
    pdf.setFillColorRGB(255, 0, 0)
    pdf.drawText(v_text17) 
    pdf.setLineWidth(1)  
    pdf.line(40, 220, 550, 220)

    pdf.showPage()
    pdf.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=fileName)


