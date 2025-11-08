from django.db import models
from orders import PENDING,PROCESSING,COMPLETED,CANCELLED

class Order(models.Model) :
   name = models.ChaField(max_length = 50, unique = True)

    def __str__(self):
         return self.name

