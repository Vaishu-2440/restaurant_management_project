from django.db import models
frm .utils import generate_unique_order_id

class Order(models.Model) :
    order_id = models.CharField(max_length = 20, unique = True, editable = False)

    def save(self, *args, **kwargs) :
        if not self.order_id :
            self.order_id = generate_unique_order_id()
        super().save(*args, **kwargs)

