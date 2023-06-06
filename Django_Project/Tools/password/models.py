from django.db import models
from django.utils import timezone
# Create your models here.
# class AllTasks(models.Model):


class Pass(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    addDate = models.DateField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.password