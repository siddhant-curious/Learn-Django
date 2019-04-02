from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=180)
    pub_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=180)
    votes = models.IntegerField(default=0)