from django.db import models
from .models import MenuItem

class DailySpecial(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    is_active = models.BooleanField(default = True)

    def get_random_special():
        qs = DailySpecial.objects.filter(is_active = True)
        if qs.exists() :
             return qs.order_by('?').first()
        return None
    
    def __str__self() :
        return self.name
