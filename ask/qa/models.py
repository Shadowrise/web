# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')

class Question(models.Model):
  objects = QuestionManager()
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(blank=True)
  rating = models.IntegerField()
  author = models.OneToOneField(User)
  likes = models.OneToManyField(User)
 
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(blank=True)
  question = models.OneToOneField(Question)
  author = models.OneToOneField(User)
  
