# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

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
  author = models.OneToOneField(User, related_name="author")
  likes = models.ManyToManyField(User, related_name="likes")
 
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  question = models.OneToOneField(Question)
  author = models.OneToOneField(User)
  
