from django.urls import path
from exam.views import CreateExamView, DoExamView, ActionExamView, PublicExamView, AllExams

urlpatterns = [
    path('create', CreateExamView.as_view()),
    path('public/<slug:short_name>/<do>', PublicExamView.as_view()),
    path('all-exams', AllExams.as_view()),
    path('<do>', DoExamView.as_view()),
    path('<slug:short_name>/<action>', ActionExamView.as_view()),
]
