"""
from django.db import models

class Order(models.Model) :
    STATUS_PENDING = "PENDING"
    STATUS_COMPLETED = "COMPLETED"

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETED, 'Completed')
    ]

    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = STATUS_PENDING)

    def mark_as_completed(self) :
        self.status = self.STATUS_COMPLETED
        self.save()

    def __str__(self) :
        return f"Order #{self.id} - {self.status}"


from django.db import models

class Order(models.Model) :
    total_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    status = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)

class Order(models.Model) :
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
    ]

    order_id = models.CharField(max_length = 20, unique = True)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'Pending')
    total_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return self.order_id
"""
from django.db import models
from decimal import Decimal

from home.models import MenuItem

class OrderItem(models.Model) :
    order = models.ForeignKey(Order, related_name = "items", on_delete = models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.DecimalField(max_digits = 10 , decimal_places = 2)

    def __str__(self) :
        return f"{self.quantity} X {self.menu_item.name}"
"""
class Order(models.Model) :
    STATUS_PENDING = 'Pemding',
    STATUS_PROCESSING = 'Processing',
    STATUS_DELIVERED = 'Delivered',
    STATUS_CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'PENDING'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_DELIVERED, 'Delivered'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    order_id = models.CharField(max_length = 20, unique = True)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = STATUS_PENDING
    )

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return self.order_id

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

from django.db import models

class Order(models.Model) :
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'PENDING'
    )

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return f"Order #{self.id}"
  
class OrderManager(models.Model) :
    def with_status(self, status) :
        return self.filter(status = status)

from django.db import models

class Order(models.Model) :
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )
    user = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES)
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)

    def calculate_total_revenue(cls) :
        result = cls.objects.filter(status = 'Completed').aggregate(
            total_revenue = Sum('total_amount')
        )
        
        return result['total_revenue'] or 0

   
    objects = OrderManager()

    def __str__(self) :
        return f"Order #{self.id} - {self.status}"
    """