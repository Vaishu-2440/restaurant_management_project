from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from home.models import MenuItem
from home.serializers import IngredientSerializer

class MenuItemIngredientsView(RetrievAPIView) :
    queryset = MenuItem.objects.all()

    def get(self, request, pk, *args, **kwargs) :
        try :
            menu_item = self.get_object()
        except MenuItem.DoesNotExist :
            return Response({"error" : "MenuItem not found"}, status = status.HTTP_404_NOT_FOUND)
        
        ingredients = menu_item.ingredients.all()
        serializer = IngredientSerializer(ingredients, many = True)
        return Response(serializer.data)