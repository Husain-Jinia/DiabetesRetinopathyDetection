#basic django imports
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic import  CreateView
from .forms import DiabetesbasicPredictionForm, PredictionForm
from .models import *

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

#document generation  
from django.http import FileResponse, QueryDict
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont



def home(request):
    return render(request, 'home.html')

# ******************************************************************************************
# Form for dummy prediction model
# ******************************************************************************************

def predictor(request):
    forms_pk = None
    
    form= PredictionForm(request.POST )
    context = {'form':form }
    if form.is_valid():
        form.save()
        x = form.save()
        forms_pk = x.pk
        return redirect(f'/result/'+ str(forms_pk))
    return render(request,'screening.html',context)
    
#*******************************************************************************************
# Model for dummy prediction model
#*******************************************************************************************

def result(request,pk):
    # dummy model
    data = pd.read_csv(r"/home/husain/Projects/IBM-mini-project/predictor/archive/diabetes.csv")
    pk = int(pk)
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]

    values = DiabetesData.objects.get(pk=pk)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(values.pregnancies)
    val2 = float(values.glucose)
    val3 = float(values.blood_pressure)
    val4 = float(values.skin_thickness)
    val5 = float(values.insulin)
    val6 = float(values.pregnancies)
    val7 = float(values.pregnancies)
    val8 = float(values.pregnancies)

    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    result=""
    if pred == [1]:
        result = "POSITIVE"
        # nearby doctor suggestions
        data = suggestion()
        return render(request, 'result.html',{'result':result,'values':values, 'data':data})
    else:
        result="NEGATIVE"
        data = suggestion()
        return render(request, 'result.html', {'result':result,'values':values, 'data':data}) 

#*****************************************************************************************
# Mapping out document coordinates
#*****************************************************************************************

def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')

#*******************************************************************************************
# pdf generation for dummy model
#******************************************************************************************* 

def result_pdf(request,pk): 
    buf = io.BytesIO() 
    fileName = 'Diabetes_results.pdf'
    logo = "Di - Free - Se"
    documentTitle = 'Diabetes Basic'
    pdf = canvas.Canvas(buf,fileName)
    pdf.setTitle(documentTitle)
    title = 'Diabetes diagnosis report'
    factors="factors"
    values_text = "Values"

    

    description = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam id neque libero. turpis dipiscing elit. ", 
    "sodales velit Proin non fermentum libero, ut mollis felis. In dictum nec turpis turpis dipiscing elit."]

    symptoms_title = 'Diabetes  symptoms'

    disclaimer = ["Please don't treat this document as your final diagnosis report. Please", 
    "consult your nearest ophthalmologist before getting any further treatment"]

    diagnosis_title='Your diagnosis'

    pegnancies = 'pregnancies '
    glucose = 'glucose '
    blood_pressure = 'blood pressure '
    skin_thickness = 'skin thickness '
    insulin = 'insulin '
    BMI = 'bmi '
    DPF = 'Diabetes Pedigree function '
    age = 'age '
    result = 'result '


    pdf.setFillColorRGB(241/256,244/256,247/256)
    pdf.rect(0,0,652,792, stroke=0,fill=1)

    pdf.rotate(60) # rotate by 45 degree 
    pdf.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK
    pdf.setFont("Helvetica", 100) # font style and size
    pdf.drawString(2*inch, -1*inch, "DI-FREE-SE") # String written 
    pdf.rotate(-60) # restore the rotation 

    patient_data = DiabetesData.objects.get(pk=pk)
    
    preg_data = patient_data.pregnancies
    glucose_data = patient_data.glucose
    bp_data = patient_data.blood_pressure
    st_data = patient_data.skin_thickness
    insulin_data = patient_data.insulin
    BMI_data = patient_data.BMI
    DPF_data = patient_data.DPF
    age_data = patient_data.age
    result_data = 'POSITIVE'

    pdf.setLineWidth(0.2)

    pdf.setFillColorRGB(45/256, 52/256, 82/256)
    pdf.rect(0,680,800,700,stroke=0,fill=1)
    pdf.setFillColor(colors.whitesmoke)
    pdf.setFont("Helvetica-Bold", 30)
    logo_text = pdf.beginText(30,746)
    logo_text.textLine(logo)
    pdf.drawText(logo_text)
    pdf.setFillColor(colors.white)
    text_desc = pdf.beginText(30, 720)
    text_desc.setFont("Helvetica", 11)
    
    for line in description:
        text_desc.textLine(line)
    pdf.drawText(text_desc)


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
    text9 = pdf.beginText(50,360)



    text0.textLine(factors)
    pdf.drawText(text0)
    text1.textLine(pegnancies)
    text2.textLine(glucose)
    text3.textLine(blood_pressure)
    text4.textLine(skin_thickness)
    text5.textLine(insulin)
    text6.textLine(BMI)
    text7.textLine(DPF)
    text8.textLine(age)
    text9.textLine(result)
    
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
    v_text9 = pdf.beginText(480,360)

   

    v_text0.textLine(values_text)
    pdf.drawText(v_text0)
    v_text1.textLine(preg_data)
    v_text2.textLine(glucose_data)
    v_text3.textLine(bp_data)
    v_text4.textLine(st_data)
    v_text5.textLine(insulin_data)
    v_text6.textLine(BMI_data)
    v_text7.textLine(DPF_data)
    v_text8.textLine(age_data)
    v_text9.textLine(result_data)


    pdf.drawText(text1)
    pdf.drawText(text2)
    pdf.drawText(text3)
    pdf.drawText(text4)
    pdf.drawText(text5)
    pdf.drawText(text6)
    pdf.drawText(text7)
    pdf.drawText(text8)
    pdf.drawText(text9)

    pdf.drawText(v_text1)
    pdf.drawText(v_text2)
    pdf.drawText(v_text3)
    pdf.drawText(v_text4)
    pdf.drawText(v_text5)
    pdf.drawText(v_text6)
    pdf.drawText(v_text7)
    pdf.drawText(v_text8)
    pdf.setFillColorRGB(255, 0, 0)
    pdf.drawText(v_text9) 
    pdf.setLineWidth(1)  
    pdf.line(40, 380, 550, 380)


    pdf.setFillColorRGB(241/256,244/256,247/256)
    pdf.rect(60,30,500,50,stroke=1,fill=1)

    pdf.setFillColor(colors.black)
    text_disc = pdf.beginText(140, 60)
    text_disc.setFont("Helvetica", 11)
    for line in disclaimer:
        text_disc.textLine(line)
    pdf.drawText(text_disc)


    pdf.showPage()
    pdf.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=fileName)


#************************************************************************************
# nearby doctor suggestions using 
# ipify API (user ip extraction) 
# ip-api (location details) 
# and Photon api (geolocation)
#************************************************************************************

def suggestion():
    ip = requests.get('http://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    longitude = str(location_data['lat'])
    latitude = str(location_data['lon'])
    suggestions = requests.get('https://photon.komoot.io/api',params={'lat':latitude,'lon':longitude,'q':'hospital','limit':"3"})
    suggestion_data = json.loads(suggestions.text)
    data = suggestion_data['features']
    print(data)
    return data

# *************************************************************************************
# diabetes basic form
# *************************************************************************************   

def diabetesbasic(request):
    forms_pk = None
    
    form= DiabetesbasicPredictionForm(request.POST )
    
    context = {'form':form }
    if form.is_valid():
        form.save()
        x = form.save()
        forms_pk = x.pk

        return redirect(f'/diabetesbasicresult/'+ str(forms_pk))
    return render(request,'diabetesbasicpred.html',context)

# *************************************************************************************
# diabetes basic model and results
# *************************************************************************************   

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
        return render(request, 'diabetesBasicResult.html',{'result':result,'values':values, 'data':data})
    else:
        result="NEGATIVE"
        return render(request, 'diabetesBasicResult.html', {'result':result,'values':values}) 


