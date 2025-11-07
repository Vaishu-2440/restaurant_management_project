import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_management_settings")
django.setup()

from home.models import menucategory
categories = menucategory.objects.all().values('name')

print(json.dumps(list(categories), indent = 2))