from decimal import Decimal, ROUND_HALF_UP

def calculate_tip_amount(order_total, tip_percentage) :
    total = Decimal(order_total)
    percentage = Decimal(tip_percentage) / Decimal(100)

    tip_amount = total * percentage

    return tip_amount.quantize(Decimal("0.01"), rounding = ROUND_HALF_UP)