from django.db import models

class Movie_Info(models.Model):
    title = models.CharField(max_length=25)
    summary = models.TextField()
    running_time = models.IntegerField()