from django.db import models


# Create your models here.
class Project(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
