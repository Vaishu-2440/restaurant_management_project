from rest_framework import serializers
from .models import Review

class ReviewSerializer(serialiers.ModelSerializer) :
    user_name = serializers.CharField(sorce = 'user.username', read_only = True)

    class Meta :
        model = Review
        fields = ['user_name', 'rating', 'created_at', 'comment']