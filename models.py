from __future__ import unicode_literals

from django.db import models
from django.core import validators

class Question(models.Model):
    qu_id    = models.AutoField(primary_key=True, db_column='qu_id')
    qu_text  = models.TextField(default='')
    type     = models.CharField(max_length=20)

class Answer(models.Model):
    qu_id     = models.ForeignKey('Question', on_delete=models.CASCADE, db_column='qu_id', default=1, null=True)
    answer_set= models.ForeignKey('AnswerSet', on_delete=models.CASCADE, db_column='answer_set', default=1, null=True)
    value     = models.TextField()
    

class AnswerSet(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    uid       = models.ForeignKey('People', on_delete=models.CASCADE, default=1, db_column='uid', null=True)
    emp_id    = models.ForeignKey('Employee', on_delete=models.CASCADE, default=1, db_column='emp_id', null=True)

class People(models.Model):
    uid = models.IntegerField(primary_key=True)

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    unit   = models.CharField(max_length=2)