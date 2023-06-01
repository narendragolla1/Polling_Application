from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    
    FormView,
    
)
from main import forms
from django.views.generic.detail import BaseDetailView
from main import models
# Create your views here.
class Index(ListView):
    model=models.Question 
    template_name='main/index.html'
    
class Question(BaseDetailView,FormView):
    model=models.Question
    template_name='main/components/question.html'  
    form_class=forms.AnswerForm
    
def form_vaild(self,form):
    obj=form.save(commit=False)
    obj=self.request.user
    obj.save()
    return HttpResponseRedirect('/')




    
