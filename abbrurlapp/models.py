from django.db import models

# Create your models here.
class abbrurls(models.Model):
    urls= models.CharField(max_length=10000)
    lid= models.CharField(max_length=15)