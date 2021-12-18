from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=200)
    days = models.IntegerField(null=True)
    till_date = models.DateField(null=True)
    price = models.BigIntegerField()
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    selling_points = models.TextField(null=True)
    description = models.TextField(null=True)
    exam = models.ForeignKey("exam.Exam", related_name="exam_subscription", on_delete=models.CASCADE)
    created_by = models.ForeignKey("auth_api.User", related_name="subscription_creater", on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    limited_time_to = models.DateField(null=True)

    def __str__(self):
        return f"{self.id} {self.name} {self.days} {self.price}"
        
    class Meta: 
        ordering = ('-id',)

class SubscriptionQuestionCategory(models.Model):
    evaluation_cost = models.FloatField(default=0.0)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.name} {self.evaluation_cost}"
    
class SubscriptionQuestionAllowence(models.Model):
    subscription = models.ForeignKey(Subscription, related_name="subscription_allowences", on_delete=models.CASCADE)
    category = models.ForeignKey(SubscriptionQuestionCategory, related_name="allowences_category", on_delete=models.SET_NULL, null=True)
    secondary_id = models.FloatField(null=True)
    subject_name = models.CharField(max_length=100)
    question_number = models.IntegerField()
    frequency = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.id} {self.subscription.name} {self.subject_name} {self.question_number}"
    
class ManagerEdits(models.Model):
    _type = models.CharField(max_length=30, default="Create")
    note = models.TextField(null=True)
    content = models.TextField()
    content_bkp = models.TextField()
    created_by = models.ForeignKey("auth_api.User", related_name="subscription_creating_manager", on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)


class SubscriptionPaymentDetails(models.Model):

    subscription = models.ForeignKey(Subscription, related_name="subscription_payment_details", on_delete=models.SET_NULL, null=True)
    subscription_subscribed = models.ForeignKey("student.StudentSubscriptionRecord", related_name="subscription_payment_details", on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey("auth_api.User", related_name="subscribed_student", on_delete=models.CASCADE)
    order_id = models.TextField(null=True)
    order_obj = models.TextField(null=True)
    receipt_id = models.TextField(null=True)
    payment_id = models.TextField(null=True)
    signature = models.TextField(null=True)
    is_paid = models.BooleanField(default=False)
    last_saved = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.order_id} - {self.receipt_id} - {self.payment_id} : {self.subscription} : {self.student.email}"
        
    class Meta: 
        ordering = ('-last_saved',)
