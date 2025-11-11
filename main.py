import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_management_settings")
django.setup()

from home.models import MenuCategory

def main():
    """Fetch and print all menu categories as json."""

    categories = MenuCategory.objects.all().values('name')
    data = list(categories)
    print (json.dumps(data, indent = 2))

if __name__ == "__main__":
    main()