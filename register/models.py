from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(upload_to="hosting", null=True, blank=True)
    invoice = models.CharField(max_length=25, null=True, blank=True)
    balance = models.IntegerField(default=0)
    referal = models.IntegerField(default=0)
    lang = models.CharField(max_length=3, blank=True, null=True)
    
class BalanceHistoryModel(models.Model):
    STATUS = (
        ('waiting','waiting'),
        ('completed','completed'),
        ('canceled','canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=50, default='waiting') 
    payment = models.CharField(max_length=150)
    check_id = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)