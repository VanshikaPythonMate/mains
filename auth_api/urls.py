from django.urls import path
from .views import Signin, Signup, ValidateToken, Verify, ChangePassword, DoUser, Do

urlpatterns = [
    path('signin', Signin.as_view()),
    path('signup', Signup.as_view()),
    path('verify/<type>', Verify.as_view()),
    path('validate', ValidateToken.as_view()),
    path('change-password', ChangePassword.as_view()),
    path('<int:uid>/<do>', DoUser.as_view()),
    path('<do>', Do.as_view()),
]
