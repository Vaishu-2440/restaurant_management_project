from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from home.models import MenuItem
from home.serializers import MenuItemSerializer

class MenuItemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50

class MenuItemSearchViewSet(viewsets.ViewSet) :
    pagination_class = MenuItemPagination
    
    def list(self, request) :
        query = request.GET.get('search', '')
        items = MenuItem.objects.filter(name__icontains = query)
        paginator = self.pagination_class()
        paginated_items = paginator.paginate_queryset(items, request)
        serializer = MenuItemSerializer(paginated_items, many = True)
        return paginator.get_paginated_response(serializer.data)

    