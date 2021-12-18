from django.urls import path
from .views import AddEvaluationView, DoEvaluationView, MyEvaluationView, DoEvaluationsView

urlpatterns = [
    path('add-new', AddEvaluationView.as_view()),
    path('my-evaluations/<which>', MyEvaluationView.as_view()),
    path('<int:evaluation_id>/<do>', DoEvaluationView.as_view()),
    path('<slug:do>', DoEvaluationsView.as_view()),
]
