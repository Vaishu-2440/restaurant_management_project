def format_currency(amount, currency_symbol = '$'):
    try :
        return f"{currency_symbol}{float(amount):.2f}"

    except (TypeError, ValueError) :
        return f"{currency_symbol}0.00"

from datetime import time
from django.utils.timezone import now
from .models import DailyOperatingHours

def is_restaurant_open1() :
    current_time = now().time()
    current_day = now().strftime('%A').lower()
    try :
        today_hours = DailyOperatingHours.objects.get(day_of_week = current_day)
    except DailyOperatingHours.DoesNotExist :
        return False

    if today_hours.opening_time < current_time < today_hours.closing_time :
        return True
    return False

def estimate_table_turnover_time(table_capacity : int) -> int :
    if table_capacity <= 2 :
        return 60
    elif table_capacity <= 4 :
        return 90
    else :
        return 120
        
from home.models import Reservation
import string
import random

def generate_reservation_confirmation_number(length = 10) :
    characters = string.ascii_uppercase + string.digits

    while True :
        confirmation_number = ''.join(random.choices(characters, k = length))

        if not Reservation.objects.filter(confirmation_number = confirmation_number).exists() :
            return confirmation_number


from django.utils import timezone
from datetime import datetime

def is_restaurant_open() :
    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()

    if current_day >= 5 :
        return False
    opening_time = time(9, 0)
    closing_time = time(22, 0)

    return opening_time <= current_time <= closing_time

from .models import Table

def get_available_tables_by_capacity(num_guests) :

    if not isinstance(num_guests, int) or num_guests <= 0 :
        return Table.objects.none()

    return Table.objects.filter(
        is_available = True,
        capacity__gte = num_guests
    )

from datetime import datetime
from home.models import DailyOperatingHours

def is_valid_reservation_time(reservation_datetime : datetime) -> bool :
    if not reservation_datetime :
        return False

    try :
        day_of_week = reservation_datetime.weekday()
        reservation_time = reservation_datetime.time()

        operating_hours = DailyOperatingHours.objects.get(
            day_of_week = day_of_week
        )

        return (
            operating_hours.opening_time
            <= reservation_time
            <= operating_hours.closing_time
        )

    except DailyOperatingHours.DoesNotExist :
        return False

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
            
            return f"{country_code} ({main_number[:3]}) {main_number[3:6]} - {main_number[6:]}"
        
        return phone_number

    except Exception :
        return phone_number


import re

def is_valid_email(email):
    if not email or not isinstance(email, str):
        return False
    email_pattern = r'^[a-zA-Z0-9_,+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-.]+$'
    return bool(re.match(email_pattern, email))
    
import smtplib
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
        MenuItem.objects.values_list("cuisine_names", flat = True)
        .distinct()
        .order_by("cuisine_names")
    )
    return list(cuisine_names)

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



























