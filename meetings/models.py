from django.db import models
from datetime import datetime

class Meeting(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(default=datetime.now)
    estimated_end = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.title


