from django import forms

class AskForm(forms.Form):
  title = forms.CharField(max_length=100)
  text = forms.CharField(widget=forms.Textarea)
  
  def save(self):
    ask = Ask(**self.cleaned_data)
    ask.save()
    return ask
  
class AnswerForm(forms.Form):
  title = forms.CharField(max_length=100)
  question = forms.IntegerField()
  
  def save(self):
    answer = Answer(**self.cleaned_data)
    answer.save()
    return answer
  
