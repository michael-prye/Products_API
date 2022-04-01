from decimal import MAX_EMAX
from django.db import models
from products.models import Product

class Review(models.Model):
    reviewer_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    number_rating = models.IntegerField()
    product_id =models.ForeignKey(Product, on_delete=models.CASCADE)