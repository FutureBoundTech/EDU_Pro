from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    img = models.ImageField()
    d_img = models.ImageField()
    info = models.CharField(max_length=100)
    price = models.IntegerField()