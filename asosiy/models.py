from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    title = models.CharField(max_length=20)
    time = models.DateField()
    description = models.CharField(max_length=300)
    status = models.BooleanField()
    foydalanuvchi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.title}"