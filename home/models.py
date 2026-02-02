"""
from django.db import models

class Restaurant(models.Model) :
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self) :
        return self.name

class HolidayHours(models.Model) :
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete = models.CASCADE,
        related_name = 'holiday_hours'
    )
    date = models.DateTimeField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    description = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        help_text = "E.g. Christmas Day, New Year Eve"
    )
    class Meta :
        unique_together = ("restaurant", "date")
        ordering = ["date"]
    
    def __str__(self) :
        return f"{self.restaurant.name} - {self.date}"

from django.db import models

class Table(models.Model) :
    table_number = models.CharField(
    max_length = 50, 
    unique = True, 
    help_text = "Unique identifier like 'Table I' or 'Bar seat 5' "
    )
    capacity = models.IntegerField(
        help_text = "Maximum number of guests the table can seat"
    )
    is_available = models.BooleanField(
        default = True,
        help_text = "Is this table currently available for reservation?"
    )

    def __str__(self) :
        return f"{self.table_number} (Capacity: {self.capacity})"

from django.db import models

class MenuItem(models.Model) :
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)

    is_vegetarian = models.BooleanField(default = False)

    def __str__(self) :
        return self.name

from django.db import models

class Ingredient(models.Model) :
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = True)

    def __str__(self) :
        return self.name

from django.db import models

class Staff(models.Model) :
    CHEF = "CHEF"
    WAITER = "WAITER"
    MANAGER = "MANAGER"

    ROLE_CHOICES = [
        (CHEF, "Chef"),
        (WAITER, "Waiter"),
        (MANAGER, "Manager"),
    ]
    
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 20, choices = ROLE_CHOICES)
    contact_email = models.EmailField(unique = True)

    def __str__(self) :
        return f"{self.first_name} {self.last_name} ({self.role}) "
"""
from django.db import models
from django.utils import timezone

class  DailySpecial(models.Model) :
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    is_available = models.BooleanField(default = True)
    date = models.DateField(default = timezone.now().date)

    def __str__(self) :
        return f"{self.name} - {self.date}"
"""
from django.db import models

class Restaurant(models.Model) :
    max_capacity = models.IntegerField(null = True)

    objects = MenuItemManager()

    def __str__(self) :
        return self.name
        
from django.conf import settings 
from django.db import models

class Feedback(models.Model) :
    user = models.ForeignKey(
        settings.AUTH_USER.MODEL,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'feedbacks'
)

 from django.db import models 
from rest_framework.viewsets import ModelViewSet
from .models import Ingredient
from .serializer import InredientSerializer

class IngredientViewSet(ModelViewSet) :
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

from django.db import models

class CustomerProfile(models.Model) :
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, blank = True, null = True)

    def get_full_name(self) :
        first = self.first_name or ""
        last = self.last_name or ""
        full_name = f"{first} {last}".strip()

        return full_name

from django.db import models
from django.utils import timezone

class DailySpecial(models.Model) :
    menu_item = models.ForeignKey(
        'MenuItem',
        on_delete = models.CASCADE,
        related_name = 'daily_specials'
    )
    date = models.DateField()
    class Meta :
        unique_together = (('menu_item', 'date'))
        ordering = ['-date']

    def __str__(self) :
        return f"{self.menu_item.name} - {self.date}"

from django.db import models

class Cuisine(models.Model) :
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self) :
        return self.name

 from .models import Cuisine

class Cuisine(models.Model) :
    name = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    cuisine = models.ForeignKey(
        Cuisine,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    def __str__(self) :
        return self.name

from django.db import models

class Cuisine(models.Manager) :
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name


from django.db import models

class Restaurant(models.Model) :
    name = models.CharField(max_length = 100)
    capacity = models.IntegerField(null =True, blank = True, default = 0)

    def __str__(self) :
        return self.name
 

from django.db import models

class MenuCategory(models.Model) :
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self) :
        return self.name    

from django.db import models

class Table(models.Model) :
    table_number = models.IntegerField(unique = True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default = True)
    location = models. CharField(max_length = 100)

    max_seats = models.IntegerField(default = 4)

    def __str__(self) :
        return f"Table {self.table_number} (Capacity : {self.capacity})"

from django.db import models

class MenuItem(models.Model) :
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    description = models.TextField(blank = True, null = True)

    is_featured = models.BooleanField(
        default = False,
        help_text = "Mark this item as featured for promotions and highlights."
    )

    def __str__(self) :
        return self.name
   
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
    user = models.ForeignKey(User, on_delete = models.CASCADE)
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

    def __str__(self) :
        return self.name

from django.db import models

class MenuCategory(models.Model) :
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name

from django.db import models

class MenuItem(models.Model) :
    name = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    description = models.TextField()
    category = models.ForeignKey(MenuCategory, on_delete = models.CASCADE)
    is_available = models.BooleanField(default = True)

    is_glutten_free = models.BooleanField(
        default = False, 
        help_text = 'Indicates of the menu item is glutten-free'
    )

    def __str__(self) :
        return self.name

class MenuCategory(models.Model) :
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self) :
        return self.name

from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model) :
    name = models.CharField(max_length = 255)

class UserReview(models.Model) :
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete = models.CASCADE,
    )
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return f"{self.user.username} - {self.menu_item.name} Review"

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









