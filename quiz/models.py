from django.db import models

# 퀴즈 모델 만들기 
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()