from django.db import models

# Create your models here.

class Box:
    id: int
    name: str
    details: str

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)  # Provide a default value