from django.urls import path
from subscription.views import CreateSubscriptionView, DoSubscriptionView, SubscriptionView

urlpatterns = [
    path('create', CreateSubscriptionView.as_view()),
    path('<do>', DoSubscriptionView.as_view()),
    path('<int:eid>/<do>', SubscriptionView.as_view()),
]
