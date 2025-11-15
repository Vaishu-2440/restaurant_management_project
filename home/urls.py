from django.urls import path
from .views import FeaturedMenuItemsView

urlpatterns = [
    path('featured-menu-items/', FeaturedMenuItemsView.as_view(), name = 'featured-menu-items'),
]