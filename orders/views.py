"""from .utils import generate_unique_order_id
from .models import Order
from rest_framework.generics import ListAPIView
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from rest_framework.decorators import api_view

class UpdateOrderStatusView(APIView) :
    def post(self, request, *args, **kwargs) :
        order_id = request.data.get("order_id") 
        new_status = request.data.get("status")

        if not order_id or not new_status :
            return Resposne(
                {"error" : "order_id and status are required"},
                status = status.HTTP_400_BAD_REQUEST
            )

        allowed_status = [choice[0] for choice in Order.STATUS_CHOICES]
        if new_status not in allowed_status :
            return Response(
                {"error" : f"Invalid status. Allowed values : {allowed_status}"},
                status = status.HTTP_400_BAD_REQUEST
            )
        try :
            order = Order.objects.get(id = order_id)

        except Order.DoesNotExist :
            return Response(
                {"error" : "Order not found."},
                status = status.HTTP_404_NOT_FOUND
            )
        order.status = new_status
        order.save()

        return Response(
            {"message" : "Order status updated successfully.",
            "order_id" : order.id,
            "new_status" : order.status},
            status = status.HTTP_200_OK
        )
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
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order

def get_order_status(requets, order_id) :
    try :
        order = Order.objects.get(id = order_id)
    except OrderDoesNotExist :
        return Response (
            {"error" : "Order not found."},
            status = status.HTTP_404_NOT_FOUND
        )
    return Reponse (
        {"order_id" : order.id, "status" : order.status},
        status = status.HTTP_200_OK
    )