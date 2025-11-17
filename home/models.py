from django.db import models
from .models import MenuItem

class NutritionalInformation(models.Model):
    menu_item = models.ForeignKey (
        MenuItem,
        on_delete = models.CASCADE,
        related_name = "nutrition"
    )
    calories = models.IntegerField()
    protein_grams = models.DecimalField(max_digits = 5, decimal_places = 2)
    fat_grams = models.DecimalField(max_digits = 5, decimal_places = 2)
    carbohydrate_grams = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self) :
        return f"{self.menu_item.name} - {self.calories} kcal"