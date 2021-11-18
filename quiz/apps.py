from django.apps import AppConfig


class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField' # 에러 방지
    name = 'quiz'