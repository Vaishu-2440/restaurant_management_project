"""
from django.contrib import admin
from .models import MenuItem

def make_unavailable(modeladmin, request, queryset) :
    queryset.update(is_available = False)

    class MenuItemAdmin(admin.ModelAdmin) :
        list_display = ('name', 'price', 'is_available')
        list_filter = ('is_available')
        actions = ['action_make_unavailable']


from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin) :
    list_display = ('name', 'address', 'phone_number', 'email', 'is_active')
    search_field = ('name', 'address')
    list_filter = ('is_active')

from django.contrib import admin
from .models import Table

admin.site.register(Restaurant, RestaurantAdmin)
"""
from django.contrib import admin
from .models import DailyOperatingHours

admin.site.register(DailyOperatingHours)
# Register your models here.
