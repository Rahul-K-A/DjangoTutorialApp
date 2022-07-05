from django.shortcuts import render,get_object_or_404
from .models import Question
from django.http import HttpResponse
# Create your views here.



'''The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. 
   It returns an HttpResponse object of the given template rendered with the given context'''
def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {
            'latest_question_list': latest_question_list,
        }
        return render(request,'polls/index.html',context)

def in2(request):
    return HttpResponse("<h2> Hola todos </h2>")
# ...
'''get_object_or_404 returns an object from the database. If no object is found it returns primary key'''
'''Alternate method- get_list_or_404: Returns list of objects obtained by filter. Returns 404 is list is none'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)