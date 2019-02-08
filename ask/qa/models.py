# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class QuestionManager(models.Manager):                                          
  def new(self):
    return self.order_by('-id')
  def popular(self):
    return self.order_by('-rating')

class Question(models.Model):
  objects = QuestionManager()
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User, related_name="author", null=True)
  likes = models.ManyToManyField(User, related_name="likes")
  
  def get_url(self):
    return '/question/' + str(self.id)
  
  def __unicode__(self):
      return str(self.id)
 
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  question = models.ForeignKey(Question, related_name='answer_set')
  author = models.ForeignKey(User, null=True)

def m_login(username, password):
  try:
    user = User.objects.get(username=username)
  except User.DoesNotExist:
    return False
  if user.check_password(password):
    return False
  user = authenticate(username=username, password=password)
  if user is None:
    return False
  return True
  
def m_signup(username, email, password):
  if User.objects.filter(username=username).exists():
    return False
  user = User.objects.create_user(username, email, password)
  user.save()
  return m_login(username, password)
  
