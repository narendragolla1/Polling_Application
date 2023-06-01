from django.forms import ModelForm
from main import models

class AnswerForm(ModelForm):
    class Meta:
        model=models.Answer
        fields = ['question', 'choice']
       