from django.db import models

class LoyaltyProgram(models.Model) :
    name = models.CharField(max_length = 100, unique = True)
    points_per_dollar_spent = models.DecimalField(max_digits = 5, decimal_places = 2)
    description = models.TextField()
    is_active = models.BooleanField(default = True)

    created_at = models.DatetimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) :
        return self.name
        
"""from django.contrib.auth.models import User

class Restaurant(models.Model) :
    name = models.CharField(max_length = 200)
    address = models.TextField()
    phone_number = models.CharField(max_length = 20)
    opening_hours = models.TextField(max_length = 200)
    description = models.TextField(blank = True, null = True)

    def __str__(self) :
        return self.name

class ContactFormSubmission(models.Model) :
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add = True)

class MenuItem(models.Model) :
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_length = 8, decimal_palces = 2)
    is_available = models.BooleanField(default = True)

    def __str_(self) :
        return self.name

class MenuItem(models.Model) :
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_length = 8, decimal_places = 2)
    description = models.TextField(blank = True, null = True)
    is_daily_special = models.BooleanField(default = False)

class MenuCategory(models.Model) :
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = True, null = True)

    def __str__(self) :
        return self.name

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

from django.db import models

class Reservation(models.Model) :
    customer_name = models.CharField(max_length = 100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self) :
        return f"{self.customer_name} ({self.start_time} -> {self.end_time})"

    def get_available_slots(range_start, range_end) :

        reservations = Reservation.objects.filter(
            end_time_gt = range_start,
            start_time_lt = range_end,
        ).order_by('start_time')

        available = []
        current_start = range_start

        for res in reservations :
            if current_start < res.start_time :
                available.append((current_start, res.start_time))
            current_start = max(current_start, res.end_time)

        if current_start < range_end :
            available.append((current_start, range_end))

        return available
"""