# django imports
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic import  CreateView
from predictor.forms import DiabetesbasicPredictionForm
from predictor.models import *
from predictor.Views.Utils.DocSuggestion import suggestion

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


def pdf_generation_utils(pdf):
    logo = "Di - Free - Se" 

    description = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam id neque libero. turpis dipiscing elit. ", 
    "sodales velit Proin non fermentum libero, ut mollis felis. In dictum nec turpis turpis dipiscing elit."]

    disclaimer = ["Please don't treat this document as your final diagnosis report. Please", 
    "consult your nearest ophthalmologist before getting any further treatment"]

    pdf.setFillColorRGB(241/256,244/256,247/256)
    pdf.rect(0,0,652,792, stroke=0,fill=1)

    pdf.rotate(60) # rotate by 45 degree 
    pdf.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK
    pdf.setFont("Helvetica", 100) # font style and size
    pdf.drawString(2*inch, -1*inch, "DI-FREE-SE") # String written 
    pdf.rotate(-60) # restore the rotation 

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

    pdf.setFillColorRGB(241/256,244/256,247/256)
    pdf.rect(60,30,500,50,stroke=1,fill=1)

    
    text_disc = pdf.beginText(140, 60)
    pdf.setFillColorRGB(1, 0, 0)
    text_disc.setFont("Helvetica", 11)
    for line in disclaimer:
        text_disc.textLine(line)
    pdf.drawText(text_disc)