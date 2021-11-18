from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

# Create your views here.
@api_view(['GET']) # url
def helloAPI(request):
    return Response("hello world!")

# 주어진 갯수만큼 랜덤한 퀴즈를 반환하는 api
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True) # many=True : 다수의 데이터에서도 직렬화 진행
    return Response(serializer.data)