from django.db import models

class OrderManager(models.Model) :
    def get_active_orders(self) :
        return self.filter(status__in = ['pending', 'processing'])

class Order(models.Model) :
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', ' Cancelled'),
    )

    cutomer = models.ForeignKey('customers.Customer', on_delete = models.CASCADE, null = True, blank = True)
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'pending')
    created_at = models.DateTimeField(auto_now_add = True)

    objects = OrderManager()

    def __str__(self):
        return f"Order #{self.id} - {self.status}"


