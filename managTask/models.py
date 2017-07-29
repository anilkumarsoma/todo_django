from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Users(models.Model):
    userid = models.CharField(max_length=50) #Auto Generated
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username+" - "+self.password

class Task(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    date = models.CharField(max_length=10)
    status = models.CharField(max_length=10)