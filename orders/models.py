from django.db import models
from .order_status import OrderStatus

class Order(models.Model):
    customer_name = models.CharField(max_length = 100)
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.ForeignKey(OrderStatus, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return f"Order by {self.customer_name} - Status : {self.status}"

