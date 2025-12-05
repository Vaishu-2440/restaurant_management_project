from decimal import Decimal, ROUND_HALF_UP
import numbers

def calculate_total(self) -> Decimal :
    total = Decimal('0.00')
    try :
        from orders.utils import calculate_discount
    except Exception :
        calculate_discount = None

    for order_item in getattr(self, "order_items", self.orderitem_set).all() :
        price = Decimal(order_item.price or 0)
        quantity = Decimal(order_item.quantity or 0)
        line_total = (price * quantity)

        discount_amount = Decimal('0.00')

        if calculate_discount :
            try :
                discount = calculate_discount(order_item)
            except TypeError :
                try :
                    discount = calculate_discount(order_item.menu_item, int(order_item.quantity))
                except Exception :
                    discount = None
            
            if discount is None :
                discount_amount = Decimal('0.00')
            else :
                if isinstance(discount, Decimal) :
                    disc = discount
                elif isinstance(discount, numbers.Real) :
                    disc = Decimal(str(discount))
                else :
                    if Decimal('0') < disc < Decimal('1') :
                        disc_amount = (line_total * disc).quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)
                    else :
                        discount_amount = disc
            if discount_amount > line_total :
                discount_amount = line_total
        net_line = line_total - discount_amount
        if net_line < Decimal('0.00') :
            net_line = Decimal('0.00')
    
        total += net_line
    return total.quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)
