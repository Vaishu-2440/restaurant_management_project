from django.db import models

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASECADE, related_name = 'menu_items')
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    is_available = models.BooleanField(default = True)
    is_featured = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
