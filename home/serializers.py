from rest_framework import serializers
from .models import feedback

class FeedbackSerializer(serializers.Modelserializer) :
    class Meta :
        model = Feedback
        fields = '__all__'


"""
from rest_framework import serializers
from .models import Cuisine

class CuisineSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Cuisine
        fields = ['id', 'name']

from rest_framework import serializers
from home.models import Table

class TableSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Table
        fields = "__all__"
        
from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer) :
    class Meta :
        model = FAQ
        fields = ['id', 'question', 'answer']
        
from .models import OpeningHour

class OpeningHourSerializer(serializers.ModelSerializer) :
    class Meta :
        model = OpeningHour
        fields = ['day', 'opening_time', 'closing_time']

from .models import MenuItem

class MenuItemSearchSerializer(serializers.ModelSerializer) :
    image_url = serializers.SerializerMethodField()

    class Meta :
        model = MenuItem
        fields =['name', 'image_url']

        def get_image_url(self, obj) :
            request = self.context.get('request')
            if obj.image and request :
                return request.build_absolute_url(obj.image.url)
            return None


from .models import Restaurant, DailyOperatingHoursSerializer

class DailyOperatingHoursSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DailyOperatingHours
        fields = [
            "day",
            "open_time",
            "close_time",
            "is_closed"
        ]

class RestaurantDetailSerializer(serializers.ModelSerializer) :
    Operating_hours = DailyOperatingHoursSerializer(many = True, read_only = True)

    class Meta :
        model = Restaurant
        fields = [
            "id",
            "name",
            "address",
            "phone_number",
            "email",
            "is_active",
            "operating_hours"
        ]
from home.models import MenuItem

class MenuItemAvailabilitySerializer(serializers.ModelSerializer) :
    class Meta :
        model = MenuItem
        fields = ['id', 'is_availabile']

from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Restaurant
        fields = "__all__"

from .models import MenuCategory
from home.models import UserReview
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

from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializer.ModelSerializer) :
    class Meta :
        model = MenuCategory
        fields = ['id', 'name']

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