from django.db import models
from auth_api.models import User

class EvaluatorPaymentDetails(models.Model):

    evaluator = models.OneToOneField(User, related_name='payment_detail_of_evaluator', on_delete=models.CASCADE)
    details = models.TextField(null=True)

    def __str__(self):
        return f"{self.id} - {self.evaluator} : {self.details}"

class EvaluatorGlance(models.Model):

    evaluator = models.ForeignKey(User, related_name='glance_evaluator', on_delete=models.CASCADE)
    status = models.CharField(default="Current", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    closed_details = models.TextField(null=True)
    closed_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return f"{self.id} - {self.evaluator.email} - {self.status} - {self.last_updated}"


class GlanceEvaluationsRecord(models.Model):

    glance = models.ForeignKey(EvaluatorGlance, related_name='glance_evaluation', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('subscription.SubscriptionQuestionCategory', related_name='glance_evaluation_category', on_delete=models.CASCADE)
    evaluation = models.OneToOneField('evaluation.Evaluation', related_name='evaluation_glance', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
        unique_together = ('glance', 'evaluation',)

    def __str__(self):
        return f"{self.id} - {self.category} - {self.evaluation.id}"
        #return f"{self.id} - {self.glance.evaluator.email} - {self.glance.status} - {self.category} - {self.evaluation.id}"

class EvaluatorRating(models.Model):

    evaluator = models.OneToOneField(User, related_name='evaluator_rating', on_delete=models.CASCADE)
    ratings_total = models.FloatField(default=0)
    ratings_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.evaluator.first_name} - {self.evaluator.email} : {self.ratings_total}/{self.ratings_count}"

class EvaluatorCategoryPricing(models.Model):

    evaluator = models.OneToOneField(User, related_name='evaluator_pricing', on_delete=models.CASCADE)
    category = models.ForeignKey('subscription.SubscriptionQuestionCategory', related_name='evaluation_unique_category', on_delete=models.SET_NULL, null=True)
    cost = models.FloatField(default=0)

    def __str__(self):
        return f"{self.id} - {self.evaluator.first_name} - {self.evaluator.email} : {self.category.name}"

    class Meta:
        ordering = ('-id',)
        unique_together = ('evaluator', 'category',)







