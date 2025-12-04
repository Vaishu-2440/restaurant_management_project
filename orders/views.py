from .utils import generate_unique_order_id
from .models import Order
from rest_framework.generics import ListAPIView
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Order

def create_order(request) :
    unique_id = generate_unique_order_id()
    order = Order.objects.create(order_id = unique_id, ...)
    return Response({"order_id" : order.order_id})

class PaymentMethodListAPIView(ListAPIView) :
    serializer_class = PaymentMethodSerilaizer

    def get_queryset(self) :
        return PaymentMethod.objects.filter(is_active = True)

class CancelOrderView(APIView) :
    permission_classes = [IsAuthenticated]

    def delete(self request, order_id) :
        try :
            order = Order.objects.get(id = order_id)
        except Order.DoesNotExists :
            return Response(
                {"error" : "Order not found."},
                status = status.HTTP_404_NOT_FOUND
            )
        
        if order.user != request.user :
            return Response(
                {"error" : "You are not authorized to cancel this order."},
                status = status.HTTP_403_FORBIDDEN
            )

        if order.status in ["Cancelled", "Completed"] :
            return Response(
                {"message" : f"Order already {order.status.lower()}"},
                status = status.HTTP_400_BAD_REQUEST
            )

        order.status = "Cancelled"
        order.save()

        return Response(
            {"message" : "Order cancelled successfully."},
            status = status.HTTP_200_OK
        )


