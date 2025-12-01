import secrets
import string
from .models import Order

def generate_unique_order_id(length : int = 8) :
    characters = string.ascii_uppercase + string.digits
    while True :
        new_id = ''.join(secrets.choice(characters) for _ in range(length)) 
        if not Order.objects.filter(order_id = new_id).exists() :
            return new_id