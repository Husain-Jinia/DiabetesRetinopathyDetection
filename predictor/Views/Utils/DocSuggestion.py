# django imports
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic import  CreateView
from predictor.forms import DiabetesbasicPredictionForm
from predictor.models import *

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


def suggestion():
    ip = requests.get('http://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    longitude = str(location_data['lat'])
    latitude = str(location_data['lon'])
    suggestions = requests.get('https://photon.komoot.io/api',params={'lat':latitude,'lon':longitude,'q':'clinic','limit':"3"})
    suggestion_data = json.loads(suggestions.text)
    data = suggestion_data['features']
    print(data)
    return data