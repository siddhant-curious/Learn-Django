from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def spiderman(request):
    return HttpResponse("Spiderman does whatever a spider can")

def ironmman(request):
    return HttpResponse("Physics bends to my will")

def antman(request):
    return HttpResponse("Is afraid of the r/dankmemes")

def endingtrail(request):
    return HttpResponse("ending trail makes all the difference")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s. " % question_id)

def results(request,question_id):
    return HttpResponse("You're looking at results of question %s. " % question_id)

def vote(request,question_id):
    return HttpResponse("You're looking at vote of question %s. " % question_id)
