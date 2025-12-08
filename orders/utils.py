"""from datetime import datetime

def format_datetime(dt) :
    if dt is None :
        return ""
    return dt.strftime("%B %d, %Y at %I : %M%p")"""

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
