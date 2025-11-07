from django.shortcuts import render
from rest_framework import generics
from home.models import MenuCategory
from home.serializers import MenuCategorySerializer

class MenuCategoryListView(generics.ListAPIView):
    """ API endpoint to list all menu categories."""
    queryset = MenuCategory.objects.all()
    serialixer_class = MenuCategorySerializer