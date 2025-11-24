from django.urls import path, include
from .views import MenuItemsByCategoryView

urlpatterns = [
    path('menu/filter-by-category/', MenuItemsByCategoryView.as_view(), name = 'menu-filter-by-category'),
]