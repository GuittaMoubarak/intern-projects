from django.db import models
from django.utils import timezone
# Create your models here.
# class AllTasks(models.Model):
class Task(models.Model):
  title = models.CharField(max_length=255)
  addDate = models.DateField(default=timezone.now)
  checked = models.BooleanField(default=False)
 
  def __str__(self):
        return self.title

