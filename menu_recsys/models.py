from django.db import models

# Create your models here.
class User(models.Model):
    user_account = models.CharField(max_length=16, primary_key=True)
    user_name = models.CharField(max_length=32, unique=False, default=user_account)
    user_pwd = models.CharField(max_length=16, default="pwd", blank=False, null=False)
    user_email = models.CharField(max_length=32, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=8, null=True, blank=True)

