from rest_framework import serializers
from .models importt Order
from home.models import MenuItem
from home.serializers import MenuItemSerializer

class OrderSerializer(serializers.ModelSerializer) :
    order_item = serializer.SerializerMethodField()

    class Meta :
        model = Order
        fields = ['id', 'customer', 'status', 'created_at', 'total_price', 'order_items']

    def get_order_items(self, object) :
        return [
            {
                'item' : item.menu_item.name,
                'quantity' : item.quantity,
                'price' : item.menu_item.price
            }
            for item in obj.order_items.all()
        ]
