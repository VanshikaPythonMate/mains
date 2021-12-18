from django.db import models

# Create your models here.

class StudentSubscriptionRecord(models.Model):

    student = models.ForeignKey("auth_api.User", related_name="student_subscribed", on_delete=models.CASCADE)
    exam = models.ForeignKey("exam.Exam", related_name="student_subscribed_exam", on_delete=models.SET_NULL, null=True)
    subscription_name = models.CharField(max_length=200)
    paid = models.BigIntegerField()
    selling_points = models.TextField(null=True)
    purchase_time = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.id} {self.student.first_name} {self.exam.short_name} {self.paid}"
        
    class Meta: 
        ordering = ('-expiry_date',)

class StudentSubscriptionsQuestionsRecord(models.Model):

    subscription = models.ForeignKey(StudentSubscriptionRecord, related_name='student_subscribed_allowences', on_delete=models.CASCADE)
    category = models.ForeignKey("subscription.SubscriptionQuestionCategory", related_name="Subject_category", null=True, on_delete=models.SET_NULL)
    subject_name = models.CharField(max_length=100)
    question_number = models.IntegerField()
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} {self.subscription.student.first_name} {self.subject_name} {self.question_number}"
