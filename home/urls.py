from django.urls import path
from .views import FeaturedMenuItemsView

urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name = 'menu-categories'),
]