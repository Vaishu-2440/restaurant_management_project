from django.contrib import admin
from .models import MenuItem

# Admin action
def make_unavailable(modeladmin, request, queryset):
    queryset.update(is_available=False)

make_unavailable.short_description = "Mark selected menu items as unavailable"

# Admin configuration
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    list_filter = ('is_available',)
    actions = [make_unavailable]


#  Register model with admin
admin.site.register(MenuItem, MenuItemAdmin)
