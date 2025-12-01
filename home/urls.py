from django.urls import path, include
from .views import ContactFormSubmissionView

urlpatterns = [
    path('contact/submit/', ContactFormSubmissionView.as_view(), name = 'contact-form-submit'),
]