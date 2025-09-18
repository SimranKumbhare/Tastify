from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    password = models.EmailField(max_length = 20)
    mobile = models.CharField(max_length = 10)
    address = models.TextField(max_length = 50)

class Restaurant(models.Model):
    name = models.CharField(max_length= 20)
    picture = models.URLField(max_length = 200, default="")
    cuisine = models.CharField(max_length = 200)
    rating= models.FloatField()
