import re

def is_valid_email(email) :
    if not email or isinstance(email, str) :
        return False
    
    email_pattern = r'^[a-ZA-Z0-9_,+-]+@[a-ZA-Z0-9-]+\.[a-ZA-Z0-9-.]+$'
    return bool(re.match(email_pattern, email))

"""import smtp
from email.mime.text import MIMEText
from django.conf import settings

from home.models import MenuItem

def send_custom_email(recipient_email, subject, message_body) :
    try :
        msg = MIMEText(message_body)
        msg["Subject"] = subject
        msg["From"] = settings.EMAIL_HOST_USER
        msg["To"] = recipient_email

        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server :
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD) 
            server.sendmail(settings.EMAIL_HOST_USER, [recipient_email], msg.as_string())

        return True

    except smtplib.SMTPRecipientsRefused :
        return "Invalid Recipient email address"
    except Exception as e :
        return f"Email sending failed : {str(e)}"

def get_distinct_cuisines() :
    cuisine_names = (
        MenuItem.objects.values_list("cuisine_name", flat = True)
        .distinct()
        .order_by("cuisine_name")
    )
    return list(cuisine_name)

def calculate_discount(original_price, discount_percentage) :
    try :
        original_price = float(original_price)
        discount_percentage = float(discount_percentage)

        if original_price < 0 :
            return {"error" : "Original price cannot be negative."}

        if discount_percentage < 0 or discount_percentage > 100 :
            return {"error" : "Discount percentage must be between 0 and 100."}

        discount_amount = (discount_percentage/100) * original_price
        discount_price = original_price - discount_amount

        return round(discount_price, 2)

    except (ValueError, TypeError) :
        return {"error" : "Invalid input. Please provide numeric value."}
"""
