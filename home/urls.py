from django.urls import path, include
from .views import total_menu_items

url_patterns = [
    path('menu_items/', total_menu_items, name = 'menu-count'),
]


"""
from django.urls import path, include
from home.views import CreateReviewAPIView, MenuItemReviewsAPIView
from rest_framework.routers import DefaultRouter
from .views import ContactFormSubmissionView
from .views import DailySpecialAPIView
from .views import MenuCategoryViewSet

router = DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename = 'menu-categories')

urlpatterns = [
    path('contact/submit/', ContactFormSubmissionView.as_view(), name = 'contact-form-submit'),
    path('daily-specials/', DailySpecialAPIView.as_view(), name = 'daily-special'),
    path('', include(router.urls)),
    path('reviews/create', CreateReviewAPIView.as_view(), name = 'create-review'),
    path('reviews/<int:menu_item_id/', MenuItemReviewsAPIview.as_view(), name = 'menu-items-reviews'),
]
"""