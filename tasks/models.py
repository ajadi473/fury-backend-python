from django.db import models
from django.utils import timezone

# Create your models here.
class Tasks(models.Model):
    date_created = models.DateField(default=timezone.now)
    reference = models.CharField(max_length=50)
    task_notes = models.TextField(null=True)
    task_date = models.DateTimeField()

    class Meta:
        ordering = ['-id']
