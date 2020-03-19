from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    low_price = models.CharField(max_length=200)
    n_review = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    