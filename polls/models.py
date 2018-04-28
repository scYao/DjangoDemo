from django.db import models


# Create your models here.
class Quesetion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Quesetion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.BigIntegerField(default=0)
