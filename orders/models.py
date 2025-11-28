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

def get_unique_item_names(self) :
    item_names = set()

    for order_item in self.orderitem_set.all() :
        if order_item.menu_item :
            item_names.add(order_item.menu_item.name)
return list(item_names)

class LoyaltyProgram(models.Model) :
    name = models.CharField(max_length = 50, unique = True)
    points_required = models.IntegerField(unique = True)
    discount_percentage = models.DecimalField(max_digits = 5, decimal_places = 2)
    description = models.TextField()

    def __str__(self) :
        return self.name
