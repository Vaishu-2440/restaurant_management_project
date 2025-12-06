from django.urls import path, include
"""from .views import ContactFormSubmissionView"""
from .views import DailySpecialAPIView

urlpatterns = [
    """path('contact/submit/', ContactFormSubmissionView.as_view(), name = 'contact-form-submit'),"""
    path('daily-specials/', DailySpecialAPIView.as_view(), name = 'daily-special'),
]