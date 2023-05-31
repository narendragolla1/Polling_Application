from django.shortcuts import render
from django.views.generic import (
    ListView
)
from main import models
# Create your views here.
class Index(ListView):
    model=models.Question
    template_name='main/index.html'