from django.db import models

class PaymentMethod(models.Model) :
    name = models.CharField(max_lentgh = 50, unique = True)
    description = models.TextField(blank = True, null = True)
    is_active = models.BooleanField(default = True)

    def __str__(self) :
        return self.name
