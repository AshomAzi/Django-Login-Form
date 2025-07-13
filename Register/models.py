from django.db import models

# Create your models here.
class user(models.Model):
    firstName = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)