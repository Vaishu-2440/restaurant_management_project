"""
from django.db import models

class MenuCategory(models.Model) :
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self) :
        return self.name

"""
from django.db import models

class Table(models.Model) :
    table_number = models.IntegerField(unique = True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default = True)
    location = models. CharField(max_length = 100)

    def __str__(self) :
        return f"Table {self.table_number} (Capacity : {self.capacity}) - {self.location}"

"""
from django.db import models

class MenuItem(models.Model) :
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    cuisine = models.CharField(max_length = 50)
    is_available = models.BooleanField(default = True)
    
    def __str__(self) :
        return self.name
        
class FAQ(models.Model) :
    question = models.CharField(max_length = 255)
    answer = models.TextField()
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return self.question

from django.utils import timezone

class ReservationManager(models.Model) :

    def get_upcoming_reservation(self) :
        return self.filter(reservation_datetime__gt = timezone.now())

class Reservation(models.Model) :
    customer_name = models.CharField(max_length = 100)
    reservation_datetime = models.DateTimeField()
    guests = models.PositiveIntegerField(default = 1)

    objects = ReservationManager()

    def __str__(self) :
        return f" {self.customer_name} - {self.reservatio_datetime}"

from django.db import models
        
class MenuItem(models.Model) :
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    cuisine_type = models.CharField(max_digits = 50)
    
    def get_items_by_cuisine(cls, cuisine_type) :
        return cls.objects.filter(cuisine_type__iexact = cuisine_type)

class MenuCategory(models.Model) :
    name models.CharField(max_length = 100, unique = True )
    
    def __str__(self) :
        return self.name

from django.db import models

class MenuItem(models.Model) :
    name = models.CharField(max_length = 255, unique = True)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    image = models.ImageField(upload_to = "menu-items/", null = True, blank = True)
    category = models.ForeignKey(
        MenuCategory,
        on_delete = models.CASCADE,
        related_name = "menu_items"
    )

    allergens = models.TextField(
        blank = True,
        null = True,
        help_text = "Comma-separated list of allergens (e.g., glutten, nuts, dairy)"
    )

    def __str__(self) :
        if self.allergens :
            return f"{self.name} - (Allergens : {self.allergens})"
            
        return self.name
        
from django.db import models
class MenuItem(models.Model) :
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    description = models.TextField(blank = True)
    is_available = models.BooleanField(default = True)

    calories = models.IntegerField(
        null = True,
        blank = True,
        help_text = "Calorie count of MenuItem"
    )

    def __str__(self) :
        return self.name
        

class OpeningHour(models.Model) :
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length = 10, choices = DAYS_OF_WEEK, unique = True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self) :
        return f"{self.day} : {self.opening_time} - {self.closing_time}" 

class MenuItem(models.Model) :
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    discount_percentage = models.DecimalField(
        max_digits = 5,
        decimal_places = 2,
        default = 0.0
    )

    def get_final_price(self) :
        discount = self.discount_percentage

        if discount < 0 :
            discount = Decimal('0.0')

        elif discount > 100 :
            discount = Decimal('100.0')
        
        discount_amount = (discount/Decimal('100.0')) * self.price
        final_price = self.price - discount_amount
        return float(round(final_price, 2))

from django.contrib.auth.models import User

class UserReview(models.Model) :
    user = models.Foreignkey(User, on_delete = models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return f"{self.user.username} - {self.rating}"
  
from django.db import models
from .models import MenuItem

class Restaurant (models.Model) :
    name = models.CharField(max_length = 255, unique = True)
    address = models.TextField()
    phone_number = models.CharField(max_length = 15)

    def __str__(self) :
        return self.name

    def get_total_menu_items(self) :
        return MenuItem.objects.count()
    
class DailyOperatingHours(models.Model) :
        restaurant = models.ForeignKey(
            Restaurant,
            related_name = "operating_hours",
            on_delete = models.CASCADE
        )
        day = models.CharField(max_length = 20)
        open_time = models.TimeField()
        close_time = models.TimeField()
        is_closed = models.BooleanField(default = False)

        def __str__(self) :
            return f"{self.day} - {self.restaurant.name}"

    class LoyaltyProgram(models.Model) :
    name = models.CharField(max_length = 100, unique = True)
    points_per_dollar_spent = models.DecimalField(max_digits = 5, decimal_places = 2)
    description = models.TextField()
    is_active = models.BooleanField(default = True)

    created_at = models.DatetimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) :
        return self.name 
    
from django.db import models

class Restaurant(models.Model) :
    name = models.CharField(max_length = 255)
    opening_hours = models.CharField(
        max_length = 100,
        help_text = "Example: 11:00 AM - 11:00 PM (EST)"
        )
     description = models.TextField(blank = True, null = True)

    def __str__(self) :
        return self.name

class ContactFormSubmission(models.Model) :
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add = True)

class MenuItem(models.Model) :
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'menu_items/', null = True, blank = True)

    def __str_(self) :
        return self.name

from django.db import models

class MenuCategory(models.Model) :
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name

class MenuItem(models.Model) :
    name = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    description = models.TextField()
    category = models.ForeignKey(MenuCategory, on_delete = models.CASCADE)
    is_available = models.BooleanField(default = True)

    def __str__(self) :
        return self.name

class MenuCategory(models.Model) :
    name = models.CharField(max_length = 100, unique = True)

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