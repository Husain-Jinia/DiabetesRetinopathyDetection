from http.client import HTTPResponse
from django.shortcuts import redirect, render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from django.views.generic import  CreateView
from .forms import PredictionForm
from .models import *
import csv
from django.http import FileResponse, QueryDict
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
import json
import requests


def home(request):
    return render(request, 'home.html')

# Create your views here.
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
    

def result(request,pk):
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
        data = suggestion()
        return render(request, 'result.html',{'result':result,'values':values, 'data':data})
    else:
        result="NEGATIVE"
        return render(request, 'result.html', {'result':result,'values':values}) 
        


    

    # result_value = DiabetesData(pk=pk, result=result)
    # result_value.save()

    

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

def result_pdf(request,pk): 
    buf = io.BytesIO() 
    fileName = 'Diabetes_retinopathy_results.pdf'
    documentTitle = 'Diabetes retinopathy'
    pdf = canvas.Canvas(buf,fileName)
    pdf.setTitle(documentTitle)
    title = 'Diabetic retinopathy report'
    symptoms_title = 'Diabetes retinopathy symptoms'

    symptoms = [
    'Spots or dark strings floating in your vision (floaters)',
    'Blurred vision.',
    'Fluctuating vision.',
    'Dark or empty areas in your vision.',
    'Vision loss.'
    ]

    disclaimer = ["* Please don't treat this document as your final diagnosis report.", 
    "Please consult your nearest ophthalmologist before getting any further treatment *"]

    diagnosis_title='Your diagnosis'

    pegnancies = 'pregnancies :'
    glucose = 'glucose :'
    blood_pressure = 'blood pressure :'
    skin_thickness = 'skin thickness :'
    insulin = 'insulin :'
    BMI = 'bmi :'
    DPF = 'Diabetes Pedigree function :'
    age = 'age :'
    result = 'result :'
    
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

    drawMyRuler(pdf)

    pdf.setFont('Courier-Bold', 30)
    pdf.drawCentredString(300, 720, title)
    pdf.line(30, 700, 550, 700)
    
    pdf.setFillColorRGB(255, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    title_text = pdf.beginText(40,660)
    title_text.textLine(symptoms_title)
    pdf.drawText(title_text)

    pdf.setFillColorRGB(255, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    diagnosis_text = pdf.beginText(40,510)
    diagnosis_text.textLine(diagnosis_title)
    pdf.drawText(diagnosis_text)
    pdf.line(30, 500, 550, 500)

    text = pdf.beginText(40, 630)
    text.setFont("Courier", 12)
    text.setFillColor(colors.blue)
    for line in symptoms:
        text.textLine(line)
    pdf.drawText(text)


    text1 = pdf.beginText(50,480)
    text2 = pdf.beginText(50,460)
    text3 = pdf.beginText(50,440)
    text4 = pdf.beginText(50,420)
    text5 = pdf.beginText(50,400)
    text6 = pdf.beginText(50,380)
    text7 = pdf.beginText(50,360)
    text8 = pdf.beginText(50,340)
    text9 = pdf.beginText(50,300)

    text1.textLine(pegnancies)
    text2.textLine(glucose)
    text3.textLine(blood_pressure)
    text4.textLine(skin_thickness)
    text5.textLine(insulin)
    text6.textLine(BMI)
    text7.textLine(DPF)
    text8.textLine(age)
    text9.textLine(result)

    v_text1 = pdf.beginText(490,480)
    v_text2 = pdf.beginText(490,460)
    v_text3 = pdf.beginText(490,440)
    v_text4 = pdf.beginText(490,420)
    v_text5 = pdf.beginText(490,400)
    v_text6 = pdf.beginText(490,380)
    v_text7 = pdf.beginText(490,360)
    v_text8 = pdf.beginText(490,340)
    v_text9 = pdf.beginText(490,300)

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
    pdf.line(30, 320, 550, 320)

    text_disc = pdf.beginText(40, 250)
    text_disc.setFont("Courier", 10)
    text_disc.setFillColor(colors.blue)
    for line in disclaimer:
        text_disc.textLine(line)
    pdf.drawText(text_disc)


    pdf.showPage()
    pdf.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=fileName)

def suggestion():
    ip = requests.get('http://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    longitude = str(location_data['lat'])
    latitude = str(location_data['lon'])
    suggestions = requests.get('https://photon.komoot.io/api',params={'lat':latitude,'lon':longitude,'q':'hospital','limit':"2"})
    suggestion_data = json.loads(suggestions.text)
    data = suggestion_data['features']
    print(data)
    return data
    




    