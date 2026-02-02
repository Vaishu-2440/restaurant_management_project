from django.contrib import admin
from .models import LoyaltyProgram

class LoyaltyProgramAdmin(admin.ModelAdmin) :
  list_display = ('name', 'points_per_dollar_spent', 'is_active')
  list_filter = ('is_active',)
  search_filters = ('name',)
  
admin.site.register(LoyaltyProgram, LoyaltyProgramAdmin)
 
