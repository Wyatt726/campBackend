from django.db import models

class Camp(models.Model):
    location = models.CharField(max_length=50)
    userID = models.CharField(max_length=50)
    ReviewID = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()


# Create your models here.
