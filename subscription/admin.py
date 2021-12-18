from django.contrib import admin
from .models import Subscription, ManagerEdits, SubscriptionQuestionAllowence, SubscriptionQuestionCategory, SubscriptionPaymentDetails
admin.site.register(Subscription)
admin.site.register(ManagerEdits)
admin.site.register(SubscriptionQuestionAllowence)
admin.site.register(SubscriptionQuestionCategory)
admin.site.register(SubscriptionPaymentDetails)
