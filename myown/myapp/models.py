from django.db import models

# Create your models here.

class Feature:
    id: int
    name: str
    details: str

class Box:
    id: int
    icon: str
    name: str
    details: str