from django.urls import path, include
from rest_framework.routers imprt DefaultRouter
"""from .views import ContactFormSubmissionView"""
from .views import DailySpecialAPIView
from .views import MenuCategoryViewSet

router = DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename = 'menu-categories')

urlpatterns = [
    """path('contact/submit/', ContactFormSubmissionView.as_view(), name = 'contact-form-submit'),"""
    path('daily-specials/', DailySpecialAPIView.as_view(), name = 'daily-special'),
    path('', include(router.urls)),
]