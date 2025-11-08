from django.db import models

class Order(models.Model) :
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
         return self.name

