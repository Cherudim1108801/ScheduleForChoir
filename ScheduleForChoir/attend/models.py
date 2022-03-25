from django.db import models

# Create your models here.
class Question1(models.Model):
    question_text = models.CharField(max_length=200)

class choice(models.model):
    temperature = models.DecimalField
    question1_answer = models.BooleanField
