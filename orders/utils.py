from django.core.mail import send_mail, BadHeadedError
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
def send_order_confirmation_email(order_id, cutomer_email, customer_name = None, total_amount = None) :
    subject = f"Order Confirmation - Order #{order_id}"
    message = (
        f"Hello {customer_name if customer_name else 'Customer'},\n\n"
        f"Thank you for ordering from our restaurant!\n"
        f"Your Order(Order ID : {order_id}) has been received and is being processed.\n"
        f"Total Amount : {total_amount if total_amount else 'N/A'}\n\n"
        f"One of our team members will notify you once your order is ready.\n\n"
        f"Regards,\n"
        f"Restaurant Team"
    )
    try :
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently = False
        )
        return {"success" : True, "message" : "Email sent successfully"}
    
    except BadHeadedError :
        logger.error("Invalid header found while sending confo=ormation email.")
        return {"success" : False, "message" : "Invalid email header"}

    except Exception as e :
        logger.error(f"Error sending order confirmation email : {e}")
        return {"success" : False, "message" : str(e)}