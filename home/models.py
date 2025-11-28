from django.db import models
from django.db import Count

class MenuItemManager(models.Manager) :
    def get_top_selling_items(self, num_items = 5) :
        return self.get_queryset().annotate(
            order_count = Count('orderitem')
        ).order_by('-ordercount')[:num_items]
class MenuItem(models.Model) :
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank= True)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    available = models.BooleanField(default = True)

    objects = MenuItemManager()

class Restaurant(models.Model) :
    name = models.CharField(max_length = 255)
    address = models.TextField()
    contact = models.CharField(max_length = 20)

    operating_days = models.CharField(
        max_length = 100
        help_text = "Comma-separated list of days(e.g., Mon,Tue,Wed,Thu,Fri,Sat,Sun)",
        blank = True,
        null = True
    )

    def __str__(self) :
        return self.name