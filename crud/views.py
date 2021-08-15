from django import http
import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.

with open('crud/stock_market_data.json') as f:
    data =json.load(f)

def homePage(request):
    return render(request, 'crud/homePage.html', {'companydata':companyData.objects.all()})

def chartPage(request):
    return render(request, 'crud/lineChart.html', {'companydata':companyData.objects.all()})
