from django.db import models
from decimal import Decimal
from home.models import MenuItem

class Order(models.Model) :
    order_id = models.CharField(max_length = 20, unique = True)
    created_at = models.DateTimeField(auto_now_add)

    def __str__(self) :
        return self.order_id
    
    def calculate_total(self) :
        total = Decimal('0.00')
        for item in self.order_items.all() :
            total += item.price * item.quantity
        return total
