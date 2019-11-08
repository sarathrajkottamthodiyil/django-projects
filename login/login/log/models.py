from django.db import models



class Sign(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    conpassword = models.CharField(max_length=100)

class Log(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Save(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=200)