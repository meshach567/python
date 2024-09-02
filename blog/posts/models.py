from django.db import models
from datetime import datetime


# Create your models here.
class Post(models.Model):
    bigimage = models.ImageField(upload_to='files/covers')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    image = models.ImageField(upload_to='files/covers')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

