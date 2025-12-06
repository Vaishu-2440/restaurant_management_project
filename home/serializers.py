from rest_framework import serializers
from .models import MenuItem
from .models import MenuCategory
"""
from .models import ContactFormSubmission

class ContactFormSubmission(serializers.ModelSerializer) :
    class Meta :
        model = ContactFormSubmission
        fields = ['id', 'email', 'name', 'message', 'submitted_at']
"""

class DailySpecialSerializer(serializer.ModelSerializer) :
    class Meta :
        model = MenuItem
        fields = ['id', 'name', 'price', 'description']

class MenuCategorySerializer(serializer.ModelSerializer) :
    class Meta :
        model = MenuCategory
        fields = ['id', 'name']
