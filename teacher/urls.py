from django.urls import path
from teacher.views import CreateTeacherView, DoTeachersView, DoTeacherView

urlpatterns = [
    path('create', CreateTeacherView.as_view()),
    path('<int:tid>/<do>', DoTeacherView.as_view()),
    path('<do>', DoTeachersView.as_view()),
]
