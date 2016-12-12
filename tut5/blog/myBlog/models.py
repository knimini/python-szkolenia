from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()
