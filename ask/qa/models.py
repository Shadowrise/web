# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

class LoginResult:
  def __init__(self, success, sessid, err_msg):
    self.success = success
    self.sessid = sessid
    self.err_msg = err_msg
  
def m_login(request, username, password):
  try:
    user = User.objects.get(username=username)
  except User.DoesNotExist:
    return LoginResult(False, None, "User doesn't exist")
  if not user.check_password(password):
    return LoginResult(False, None, "Incorrect password")
  user = authenticate(username=username, password=password)
  if user is None:
    return LoginResult(False, None, "Authentication failed")
  login(request, user)
  return LoginResult(True, request.session.session_key, None)
  
def m_signup(request, username, email, password):
  if User.objects.filter(username=username).exists():
    return LoginResult(False, None, "User already exists")
  user = User.objects.create_user(username, email, password)
  try:
    user.save()
  except Exception as e: 
    return LoginResult(False, None, "User saving failed")
  return m_login(request, username, password)

  
