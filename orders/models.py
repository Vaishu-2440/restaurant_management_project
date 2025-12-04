from django.db import models

class OrderManager(models.Model) :
    def with_status(self, status) :
        return self.filter(status = status)

class Order(models.Model) :
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )
    cutomer = models.ForeignKey("accounts.Customer", on_delete = models.CASCADE)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = "pending")
    created_at = models.DateTimeField(auto_now_add = True)

    objects = OrderManager()

    def __str__(self) :
        return f"Order #{self.id} - {self.status}"
