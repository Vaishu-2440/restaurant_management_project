from django.db import models

"""
class Order(models.Model) :
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50, default = 'Pending')
    def __str__(self) :
        return f"Order #{self.id}"

    def get_total_item_count(models.self) :
        total_count = 0
        for item in self.items.all() :
            total_count += item.quantity
        return total_count


from django.contrib.auth.models import User

class Order(models.Model) :
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    order_id = models.CharField(
        max_length = 20,
        unique = True,
        db_index = True
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Pending'
    )

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return self.order_id
        
class OrderManager(models.Model) :
    def with_status(self, status) :
        return self.filter(status = status)
"""

from django.db import models

class Order(models.Model) :
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )
    cutomer = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = "pending")
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)

    def calculate_total_revenue(cls) :
        result = cls.objects.filter(status = 'Completed').aggregate(
            total_revenue = Sum('total_amount')
        )
        
        return result['total_revenue'] or 0

   """
    objects = OrderManager()

    def __str__(self) :
        return f"Order #{self.id} - {self.status}"
    """