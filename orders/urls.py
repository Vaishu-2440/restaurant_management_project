from django.urls import path
from .views import OrderDetailAPIView
from .views import PaymentMethodListAPIView
from .views import CancelOrderView

urlpatterns = [
    path ('orders/<int:id>/', OrderDetailAPIView.as_view(), name = 'order-detail'),
    path ('api/payment - methods/', PaymentMethodListAPIView.as_view(), name = 'payment-methods'),
    path ("cancel - order/<int:order_id>", CancelOrderView.as_view(), name = 'cancel-order'),
]