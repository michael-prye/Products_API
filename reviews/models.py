from decimal import MAX_EMAX
from django.db import models

class Review(models.Model):
    reviewer_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    number_rating = models.IntegerField()