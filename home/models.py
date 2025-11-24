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

    def __str__(self) :
        return self.name