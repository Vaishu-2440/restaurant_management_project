from django.db import models
from django.contrib.auth.models import User
"""
class ContactFormSubmission(models.Model) :
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add = True)

class MenuItem(models.Model) :
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_length = 8, decimal_places = 2)
    description = models.TextField(blank = True, null = True)
    is_daily_special = models.BooleanField(default = False)

class MenuCategory(models.Model) :
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self) :
        return self.name
"""

class UserReview(models.Model) :
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'reviews'
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete = models.CASCADE,
        related_name = 'reviews'
    )
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return f"{self.user.username} - {self.menu_item.name} - {self.rating}/5"
