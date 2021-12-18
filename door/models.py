from django.db import models

class NoticeBoard(models.Model):

    notice = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.notice}"

class TermsnConditions(models.Model):

    note = models.TextField()
    is_heading = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.is_heading} - {self.note}"




