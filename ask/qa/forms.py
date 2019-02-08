from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
  title = forms.CharField(max_length=100)
  text = forms.CharField(widget=forms.Textarea)
  
  def save(self):
    question = Question(**self.cleaned_data)
    question.save()
    return question
  
class AnswerForm(forms.Form):  
  text = forms.CharField(widget=forms.Textarea)
  question = forms.IntegerField()
  
  def clean_question(self):
    question_id = self.cleaned_data['question']
    return Question.objects.get(id=int(question_id))
  
  def save(self):
    answer = Answer(**self.cleaned_data)
    answer.save()
    return answer
