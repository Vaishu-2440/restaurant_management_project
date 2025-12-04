from .utils import generate_unique_order_id
from .models import Order
from rest_framework.generics import ListAPIView
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer

def create_order(request) :
    unique_id = generate_unique_order_id()
    order = Order.objects.create(order_id = unique_id, ...)
    return Response({"order_id" : order.order_id})

class PaymentMethodListAPIView(ListAPIView) :
    serializer_class = PaymentMethodSerilaizer

    def get_queryset(self) :
        return PaymentMethod.objects.filter(is_active = True)
