from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

class FeaturedMenuItemsAPIView(APIView) :
    def get(self, request) :
        featured_items = MenuItem.objects.filter(is_featured = True)
        serializer = MenuItemSerializer(featured_items, many = True)
        return Response(serializer.data)

"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem

def total_menu_items(request) :
    total_items = MenuItem.objects.filter(is_available = True).count()
    return Response({"total_menu_items" :  total_items})

from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from .models import Restaurant
from .serializers import RestaurantDetailSerializer

class RestaurantDetailAPIView(RetrieveAPIView) :
    queryset = Restaurant.objects.filter(is_active = True)
    serializer_class = RestaurantDetailSerializer

from .models import MenuCategory
from .serializers import MenuCategorySerializer
from home.models import UserReview
from rest_framework import generics, permissions
from home.serializers import UserReviewSerializer
from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import DailySpecialSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import send_custom_email

class FeedbackView(APIView) :
    def post(self, request) :
        user_email = request.data.get("email")
        subject = "Thank you for contacting us!"
        message = "We have received your message and we will get back to you soon."

        result = send_custom_email(user_email, subject, message)

        if result:
            return Response({"Message" : "Email sent successfully."})
        return Response({"error" : result}, status = 400)

class DailySpecialSerializer(ListAPIView) :
    serializer_class = DailySpecialSerializer

    def get_queryset(self) :
        return MenuItem.objects.filter(is_daily_special = True)
 
class MenuCategoryViewSet(viewsets.ModelViewSet) :
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class CreateReviewAPIView(generics.APIView) :
    serializer_class = UserReviewsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer) :
        serializer.save(user = self.request.user)

class MenuItemReviewAPIView(generics.ListAPIView) :
    serializer_class = UserReviewSerializer

    def get_queryset(self) :
        menu_item_id = self.kwargs.get("menu_item_id")
        return UserReview.objects.filter(menu_item_id = menu-item_id).order_by('-created_at')
 """




