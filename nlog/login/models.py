from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)


class Assert(models.Model):
    department = models.CharField(max_length=50)
    number = models.CharField(max_length=50,null=False,unique=True)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    position = models.CharField(max_length=50)