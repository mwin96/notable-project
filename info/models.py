from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default = '')
    kind = models.CharField(max_length=300)
    date = models.DateField(default = "2000-01-01")
    time = models.TimeField(default = datetime.now() )
    doctor = models.CharField(max_length= 300, default = 'None')
    created_at = models.DateTimeField(auto_now_add=True)

class Physicians(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default = '')