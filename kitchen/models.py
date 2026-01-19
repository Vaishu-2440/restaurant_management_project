from django.db import models

class Ingredient(models.Model) :
    name = models.CharField(max_length = 100, unique = True)
    unit_of_measure = models.CharField(max_length = 50)

    def __str__(self) :
        return self.name