from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Endpoint(models.Model):
    
    endpoint_name = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100)
    route= models.CharField(max_length=200)
    url_params = models.CharField(max_length=200, null=True, blank=True)
    supported_http_actions = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ['-id']
    