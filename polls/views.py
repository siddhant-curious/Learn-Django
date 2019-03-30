from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def spiderman(request):
    return HttpResponse("Spiderman does whatever a spider can")

def ironmman(request):
    return HttpResponse("Physics bends to my will")

def antman(request):
    return HttpResponse("Is afraid of the r/dankmemes")

def endingtrail(request):
    return HttpResponse("ending trail makes all the difference")