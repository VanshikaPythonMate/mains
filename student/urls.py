from django.urls import path
from student.views import AddSubscriptionView, DoStudentView, DoStudentsView, DoStudentExamView

urlpatterns = [
    path('add-new/<do>', AddSubscriptionView.as_view()),
    path('<do>', DoStudentsView.as_view()),
    path('<int:student_id>/<do>', DoStudentView.as_view()),
    path('<slug:exam_short_name>/<do>', DoStudentExamView.as_view()),
]
