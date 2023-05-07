from django.db import models
from django.utils import timezone

# Create your models here.

PRIORITY_CHOICES = (
    ('urgent Business', 'URGENT BUSINESS' ),
    ('fixing this today', 'FIXING THIS TODAY'),
    ('this can wait', 'THIS CAN WAIT')
)

class Task(models.Model):
    newtasks = models.CharField(max_length=500)
    post_date = models.DateTimeField(default=timezone.now)
    priority = models.CharField(max_length=50,choices = PRIORITY_CHOICES, default= 'Urgent Business', blank=True, null=True)

    def __str__(self):
        return self.newtasks


