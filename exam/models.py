from django.db import models

defaultText = "Put Your contents here."

class Exam(models.Model):
    short_name = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150, null=True)
    content1 = models.TextField(null=True, default=defaultText)
    content2 = models.TextField(null=True, default=defaultText)
    content3 = models.TextField(null=True, default=defaultText)
    content4 = models.TextField(null=True, default=defaultText)
    date_time_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey("auth_api.User", related_name="Exam_creater", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='exam_images', null=True)

    def __str__(self):
        return f"{self.id} {self.short_name}"
        
    class Meta: 
        ordering = ('-id',)

class ExamManagerRelation(models.Model):
    exam = models.ForeignKey(Exam, related_name="Exam_in_examManager", on_delete=models.CASCADE)
    manager = models.ForeignKey("auth_api.User", related_name="Manager_in_examManager", on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.id} {self.exam.short_name} managed by {self.manager.first_name} with {self.manager.email}"





