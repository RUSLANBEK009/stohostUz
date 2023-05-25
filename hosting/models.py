from django.contrib.auth.models import User
from django.db import models



class HostingTemplate(models.Model):
    name = models.CharField(max_length=255)
    site = models.IntegerField(default=1)
    domain = models.IntegerField(default=1)
    size = models.IntegerField(default=1024)
    ftp = models.IntegerField(default=1)
    db = models.IntegerField(default=1)
    db_size = models.IntegerField(default=10)
    ssh = models.BooleanField(default=True)
    
