from django.contrib.auth.models import User
from django.db import models

class Order(models.Model) :
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "orders")
    date = models.DateTimeField(auto_now_add = True)
    total_price = models.DecimalField(max_digits = 10, decimal_place = 2)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


