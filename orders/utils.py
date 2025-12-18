from decimal import Decimal, InvalidOperation
def calculate_discount(order_total, discount_percentage) :
    try :
        order_total = Decimal(order_total)
        discount_percentage = Decimal(discount_percentage)

        if order_total <= 0 or discount_percentage <= 0 :
            return Decimal('0.00')   
               
        discount_amount = order_total * (discount_percentage / (Decimal('100')))

        if discount_amount > order_total :
            return order_total
        
        return discount_amount.quantize(Decimal('0.01'))

    except (InvalidOperation, TypeError) :
        return Decimal('0.00')
 
"""
from datetime import datetime

def format_datetime(dt) :
    if dt is None :
        return ""
    return dt.strftime("%B %d, %Y at %I : %M%p")

from orders.models import Order
import logging
logger = logging.getLogger(__name__)

def update_order_status(order_id, new_status) :
    try :
        order = Order.objects.get(id = order_id)
    except Order.DoesNotExist :
        logger.error(f"Order with ID {order_id} not found")
        return False, f"Order with ID {order_id} not found."
    old_status = order.status
    order.status = new_status
    order.save()

    logger.info(
        f"Order #{order_id} status updated from '{old_status}' to '{new_status}'."
    )
 
    return True, f"Order #{order_id} status updated successfully."
"""
