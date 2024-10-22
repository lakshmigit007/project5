from django.db import models
class student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    location = models.CharField(max_length=60)

# Create your models here.
