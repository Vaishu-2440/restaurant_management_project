from django.urls import path
from .views import UserProfileUpdateAPIView

urlpatterns = [
    path("profile/update/", UserProfileUpdateAPIView.as_view, name = "profile - update"),
]