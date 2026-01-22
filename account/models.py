from django.db import models
from django.conf import settings

class CustomerProfile(models.Model) :
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name ="customer_profile"
    )
    phone_number = models.CharField(max_length = 20, blank = True, null = True)
    delivery_address = models.TextField(blank = True, null = True)

    def __str__(self) :
        return f"{self.user.username}'s Customer Profile"

""" from django.db import models
from django.contrib.auth.models import User

CUISINE_CHOICES = (
    ('italian', 'Italian'),
    ('mexican', 'Mexican'),
    ('asian', 'Asian'),
    ('vegetarian', 'Vegetarian'),
)
"""
