"""
from rest_framework import serializers
from .models import OrderItem

class UpdateOrderItemQuantitySerializer(serializers.ModelSerializer) :
    class Meta :
        model = OrderItem
        fields = ["id", "quantity"]

    def validate_quantity(self, value) :
        if value < 0 :
            raise serializers.ValidationError("Quantity must be a positive integer")
        return value
"""
from rest_framework import serializers
from orders.models import Table

class TableSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Table
        fields = "__all__"
"""
from rest_framework import serializers
from orders.models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer) :
    class Meta :
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer) :
    item = OrderItemSerializer(source = 'order_item_set', many = True)

    class Meta :
        model = Order
        fields = [
            'id',
            'created_at',
            'status',
            'total_amount',
            'items'
        ]


from decimal import Decimal, ROUND_HALF_UP
import numbers


def calculate_total(self) -> Decimal:
    total = Decimal("0.00")

    try:
        from orders.utils import calculate_discount
    except ImportError:
        calculate_discount = None

    order_items = getattr(self, "order_item", self.order_item).all()

    for order_items in order_item:
        price = Decimal(str(order_item.price or 0))
        quantity = Decimal(str(order_item.quantity or 0))
        line_total = price * quantity

        discount_amount = Decimal("0.00")

        if calculate_discount:
            try:
                discount = calculate_discount(order_item)
            except TypeError:
                try:
                    discount = calculate_discount(
                        order_item.menu_item,
                        int(order_item.quantity)
                    )
                except TypeError:
                    discount = None

            # Normalize numeric discount to Decimal
            if isinstance(discount, numbers.Real):
                discount = Decimal(str(discount))

            if isinstance(discount, Decimal):
                # Percentage discount (e.g., 0.10 = 10%)
                if Decimal("0") < discount <= Decimal("1"):
                    discount_amount = (line_total * discount).quantize(
                        Decimal("0.01"),
                        rounding=ROUND_HALF_UP
                    )
                # Flat discount (e.g., 50)
                elif discount > Decimal("1"):
                    discount_amount = discount

        # Prevent discount exceeding line total
        if discount_amount > line_total:
            discount_amount = line_total

        net_line = line_total - discount_amount
        if net_line < Decimal("0.00"):
            net_line = Decimal("0.00")

        total += net_line

    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
"""







