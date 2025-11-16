from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist
from .models import Order

def get_daily_sales_total(date) :
    try :
        orders = Order.objects.filter(created_at_date = date)
        total  = orders.aggregate(total_sum = Sum('total_price'))['total_sum']
        return total or 0

    except Exception as e :
        return 0