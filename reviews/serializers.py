from dataclasses import fields
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'reviewer_name', 'subject', 'review', 'number_rating']