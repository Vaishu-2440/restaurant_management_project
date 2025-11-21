class Ingredient(models.Model) :
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name

class MenuItem(models.Model):
    name = CharField(max_length = 100)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    ingredients = models.ManyToManyField(Ingredient, related_name = "menu_items")

    def __str__(self) :
        return self.name