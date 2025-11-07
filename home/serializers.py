from rest_framework import serializers
from home.models import MenuCategory

# Serializer for MenuCategory model
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['name']