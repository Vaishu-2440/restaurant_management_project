from .utils import generate_unique_order_id
from .models import Order

def create_order(request) :
    unique_id = generate_unique_order_id()
    order = Order.objects.create(order_id = unique_id, ...)
    return Response({"order_id" : order.order_id})