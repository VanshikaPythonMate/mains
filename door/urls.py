from django.urls import path, include
from .views import DoGeneral, DoPublic

urlpatterns = [
    path('exam/', include('exam.urls')),
    path('auth/', include('auth_api.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    # path('manager/', include('manager.urls')),
    path('evaluation/', include('evaluation.urls')),
    path('subscription/', include('subscription.urls')),
    path('general/<do>', DoGeneral.as_view()),
    path('public/<do>', DoPublic.as_view()),
]
