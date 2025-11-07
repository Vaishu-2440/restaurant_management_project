from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Dummy serializer
class MenuCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

# Dummy data
MENU_CATEGORIES = [
    {"name": "Starters"},
    {"name": "Main Course"},
    {"name": "Desserts"},
]

@api_view(['GET'])
def get_menu_categories(request):
    serializer = MenuCategorySerializer(MENU_CATEGORIES, many=True)
    return Response(serializer.data)

# To run test locally
if __name__ == "__main__":
    import json
    print(json.dumps(MENU_CATEGORIES, indent=2))
