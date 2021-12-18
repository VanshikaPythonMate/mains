from django.contrib import admin
from .models import EvaluatorPaymentDetails, EvaluatorGlance,  GlanceEvaluationsRecord, EvaluatorRating, EvaluatorCategoryPricing
admin.site.register(EvaluatorGlance)
admin.site.register(EvaluatorRating)
admin.site.register(EvaluatorPaymentDetails)
admin.site.register(GlanceEvaluationsRecord)
admin.site.register(EvaluatorCategoryPricing)

