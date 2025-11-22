from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemUpdateViewSet(viewsets.Viewset) :
    permission_classes = [IsAdminUser]

    def update(self, request, pk = None) :
        menu_item = get_object_or_404(MenuItem, pk = pk)
        serializer = MenuItemSerializer(menu_item, data = request.data, partial = False)
        if serializer.is_valid() :
            serializer.save()
            return Response(
                {
                    "message" : "MenuItem updated successfully",
                    "data" : serializer.data
                }, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)