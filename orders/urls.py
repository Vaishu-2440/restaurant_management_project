from django.urls import path
from .views import OrderDetailAPIView
from .views import PaymentMethodListAPIView

urlpatterns = [
    path ('orders/<int : id>/', OrderDetailAPIView.as_view(), name = 'order-detail'),
    path ('api/payent - methods/', PaymentMethodListAPIView.as_view(), name = 'payment_methods'),
]