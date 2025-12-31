"""
import re

def format_phone_number(phone_number) :
    try :
        if not phone_number :
            return ""

        digits = re.sub(r"\D", "", phone_number)

        if len(digits) == 10 :
            return f"({digits[:3]}) {digits[3:6]} - {digits[6:]}"

        elif len(digits) > 10 :
            country_code = digits[:-10]
            main_number = digits[-10:]
            
            return f" {country_code} ({main_number[:3]}) {main_number[3:6]} - {main_number[6:]}"
        
        return phone_number

    except Exception :
        return phone_number


def is_valid_email(email) :
    if not email or isinstance(email, str) :
        return False
    
    email_pattern = r'^[a-zA-Z0-9_,+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_pattern, email))

import smtp
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

"""
def calculate_discount(price, discount_percentage) :
    try :
        price = float(price)
        discount_percentage = float(discount_percentage)

        if price < 0 or discount_percentage < 0 or discount_percentage > 100 :
            return price

        discount_amount = price * (discount_percentage/100) 
        discount_price = price - discount_amount

        return round(discount_price, 2)

    except (ValueError, TypeError) :
        return price

