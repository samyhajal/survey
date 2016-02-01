from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import Error
import os
from survey.models import Question, Answer, AnswerSet
import sys

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def all_questions(request):
    questions = Question.objects.all()
    template = os.path.dirname(os.path.abspath(__file__)) + '/templates/all_questions.html'
    return render(request, template, {'questions' : questions})

def question(request):
    template = os.path.dirname(os.path.abspath(__file__)) + '/templates/question.html'
    return render(request, template, {})

def create(request):
    post = request.POST
    question = Question(qu_text=post['text'], type=post['type'])
    question.save()
    return HttpResponseRedirect(reverse('all_questions', args=()))

def delete(request, question_id):
    question = Question.objects.get(qu_id=question_id)
    question.delete()
    return HttpResponseRedirect(reverse('all_questions', args=()))

def edit(request, question_id):
    question = Question.objects.get(qu_id=question_id)
    return HttpResponseRedirect(reverse('all_questions', args=()))

def survey(request):
    questions = Question.objects.all()
    template = os.path.dirname(os.path.abspath(__file__)) + '/templates/survey.html'
    return render(request, template, {'questions' : questions})

def submit(request):
    post = request.POST
    qu_ids = []
    answer_set = AnswerSet()
    answer_set.save()
    for key in post.keys():
        try:
            qu_id = int(key)
            if post[key] != '':
                print(key, post[key])
                question = Question.objects.get(qu_id=qu_id)
                print(question)
                ans = Answer(qu_id=question, value=post[key], answer_set=answer_set)
                ans.save()
                print('okay')
        except ValueError:
            continue
    return HttpResponseRedirect(reverse('survey', args=()))

