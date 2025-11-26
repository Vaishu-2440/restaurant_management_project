from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin) :
    list_display = ('name', 'address', 'phone_number', 'email', 'is_active')
    search_field = ('name', 'address')
    list_filter = ('is_active')

admin.site.register(Restaurant, RestaurantAdmin)

# Register your models here.
