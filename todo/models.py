from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    newtasks = models.CharField(max_length=500)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.newtasks


