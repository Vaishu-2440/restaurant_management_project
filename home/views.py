from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsByCategoryView(APIView) :
    def get(self, request) :
        category_name = request.GET.get('category', None)

        if not category_name :
            return Response(
                {"error" : "Category query parameter is required"},
                status = status.HTTP_404_BAD_REQUEST
            )
        menu_items = MenuItem.objects.filter(category_category_name_iexact = category_name)

        serializer = MenuItemSerializer(menu_items, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)