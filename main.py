from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

class MenuCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)

menu_categories = [
    {"name" : "Starters"},
    {"name" : "Main Course"},
    {"name" : "Desserts"},
]

def get_menu_categories(request):
    serializer = MenuCategorySerializer(nenu_categories, many = True)
    return Response(serializer.data)

if __name__ == "__main__":
    import json
    print (json.dumps(menu_categories, indent = 2))