from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=20)
    time = models.DateField()
    description = models.CharField(max_length=300)
    status = models.BooleanField()
    def __str__(self):
        return f"{self.title}"