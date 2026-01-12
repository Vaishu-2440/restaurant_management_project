from django.contrib.auth.models import User
from rest_framework import serializers

class UserLoyaltySerializer(serializers.modelSerializer) :
    class Meta :
        model = User
        fields = ['loyalty_points']

"""
from django.contrib.auth.models import User
frm rest_framework import seializers

class UserProfileUpdateSerializer(serializer.ModelSerializer) :
    class Meta :
        model = User
        field = ['first_name', 'last_name', 'email']
        extra_kwargs = {
            "email" ; {"required" : "True"}
        }
"""