from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
class User(models.Model):
    user_name = models.CharField(max_length=30)
    psw = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
