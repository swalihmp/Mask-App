from email.policy import default
from django.db import models

# Create your models here.
class admins(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=20)
    key = models.CharField(max_length=5)
      
class users(models.Model):
    name = models.CharField(primary_key=True, max_length=15)
    gmail = models.EmailField()
    gender = models.CharField(max_length=5)
    password = models.CharField(max_length=20)
    key = models.CharField(max_length=45)
    
class mask(models.Model):
    type = models.CharField(max_length=30)
    rate = models.CharField(max_length=10)
    qty = models.CharField(max_length=20)
    
class order(models.Model):
    user = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    qty = models.CharField(max_length=20)
    date = models.DateTimeField()
    status = models.CharField(max_length=10, default="Pending")
    