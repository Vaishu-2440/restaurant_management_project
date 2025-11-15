from django.shortcuts import render
from rest_framework import generics
from home.models import MenuItem
from home.serializers import MenuItemSerializer

class FeaturedMenuItemsView(generics.ListAPIView):
    """ API endpoint to list all menu categories."""
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer