from django.urls import path, include
from .views import helloAPI, randomQuiz

# 퀴즈 앱에서의 url

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]