from rest_framework import serializers
from .models import MenuCategory
"""from home.models import UserReview
from .models import MenuItem
from .models import ContactFormSubmission

class ContactFormSubmission(serializers.ModelSerializer) :
    class Meta :
        model = ContactFormSubmission
        fields = ['id', 'email', 'name', 'message', 'submitted_at']

class DailySpecialSerializer(serializer.ModelSerializer) :
    class Meta :
        model = MenuItem
        fields = ['id', 'name', 'price', 'description']
"""
class MenuCategorySerializer(serializer.ModelSerializer) :
    class Meta :
        model = MenuCategory
        fields = '__all__'
"""
class UserReviewSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserReview
        fields = ['id', 'user', 'menu_item', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

    def validate_rating(self, value) :
        if value < 1 or value > 5 :
            raise serializers.ValidationError("Rating must be between 1 or 5")
        return value
"""