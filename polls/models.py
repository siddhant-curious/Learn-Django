from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=180)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date  <= timezone.now()

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=180)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text