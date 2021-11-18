from django.contrib import admin
from .models import Quiz

# 관리자 페이지에 퀴즈 모델을 register하여 관리할 수 있게 함
admin.site.register(Quiz)