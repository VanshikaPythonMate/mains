from django.db import models

class Evaluation(models.Model):

    student = models.ForeignKey("auth_api.User", related_name="worried_student", on_delete=models.CASCADE)
    evaluator = models.ForeignKey("auth_api.User", related_name="selected_evaluator", on_delete=models.SET_NULL, null=True)
    exam = models.ForeignKey("exam.Exam", related_name="for_exam", on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey("student.StudentSubscriptionsQuestionsRecord", related_name="subscribed_subscription", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("subscription.SubscriptionQuestionCategory", related_name="subscribed_subscription_que_category", on_delete=models.SET_NULL, null=True)
    subscribed_subscription = models.ForeignKey("student.StudentSubscriptionRecord", related_name="subscribed_subscription", on_delete=models.SET_NULL, null=True)
    answer_file = models.FileField(upload_to='student_asnwer_uploads', null=True)
    evaluated_file = models.FileField(upload_to='evaluator_evaluated_uploads', null=True)
    marks = models.CharField(max_length=20, default="unmarked")
    answers_count = models.IntegerField()
    student_message = models.TextField(null=True)
    evaluator_message = models.TextField(null=True)
    rating_to_evaluator = models.FloatField(null=True)
    feedback_to_evaluator = models.TextField(null=True)
    tags = models.TextField(null=True)
    status = models.CharField(max_length=50, default="Queued")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    date_time_recent = models.DateTimeField(auto_now=True)
    date_time_evaluated = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return f"{self.id} {self.student.first_name}, answers_count : {self.answers_count}"
        
    class Meta: 
        ordering = ('-id',)



