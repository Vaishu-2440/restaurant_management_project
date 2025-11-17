from django.urls import path, include
from .views import MenuItemSearchViewSet

urlpatterns = [
    path('menu/search/', MenuItemSearchViewSet.as_view({'get' : 'list'}), name = 'menu - search'),
]