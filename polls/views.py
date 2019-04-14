from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
# Create your views here.
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))
    # return render(request, 'polls/index.html', context)

def spiderman(request):
    return HttpResponse("Spiderman does whatever a spider can")

def ironmman(request):
    return HttpResponse("Physics bends to my will")

def antman(request):
    return HttpResponse("Is afraid of the r/dankmemes")

def endingtrail(request):
    return HttpResponse("ending trail makes all the difference")

def detail(request,question_id):
    try:
        quest = Question.objects.get(pk=question_id)
        context = {'question':quest}
        return render(request,'polls/question.html',context)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return HttpResponse("You're looking at question %s. " % question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})


def results(request,question_id):
    return HttpResponse("You're looking at results of question %s. " % question_id)

def vote(request,question_id):
    return HttpResponse("You're looking at vote of question %s. " % question_id)
