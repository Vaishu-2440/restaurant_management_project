from rest_framework import serializers
from .models import Order
from home.models import MenuItem
from home.serializers import MenuItemSerializer
from .models import PaymentMethod

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

class OrderStatusUpdateSerializer(serialzier.ModelSerializer) :
    class Meta :
        model = Order
        fields = ['status']

    def validate_status(self, value) :
        allowed_statuses = [choice[0] for choice in Order.STATUS_CHOICES] 
        if value not in allowed_statuses :
            raise serializers.ValidationError("Invalid status value.")
        return value

class PaymentMethodserializer(serializers.ModelSerializer) :
    class Meta :
        model = PaymentMethod
        fields = '__all__'

