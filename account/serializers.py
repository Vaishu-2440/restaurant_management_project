from rest_framework import serializers
from .models import Staff

class StaffSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Staff
        fields = '__all__'

"""
from django.contrib.auth.models import User
from rest_framework import serializers

class UserLoyaltySerializer(serializers.modelSerializer) :
    class Meta :
        model = User
        fields = ['loyalty_points']

from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileUpdateSerializer(serializer.ModelSerializer) :
    class Meta :
        model = User
        field = ['first_name', 'last_name', 'email']
        extra_kwargs = {
            "email" ; {"required" : "True"}
        }
"""