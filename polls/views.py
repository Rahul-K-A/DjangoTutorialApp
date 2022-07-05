from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        '''request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, 
        as a string. request.POST values are always strings.
        "choice" comes from the name of the input tag in the detail.html form
        '''
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #reverse looks up the url for the name as defined in urls.py
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))