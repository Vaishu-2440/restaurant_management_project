def calculate_order_total(order_items) :
    if not order_items :
        return 0
    total = 0

    for item in order_items :
        qty = item.get("quantity", 0)
        price = item.get("price", 0)

        total += qty * price
    
    return total

