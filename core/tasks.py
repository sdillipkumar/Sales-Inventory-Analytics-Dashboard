from celery import shared_task
from django.core.mail import send_mail
from .models import Product
from django.db import models
from .models import Sale, KPIReport
from django.db.models import Sum, F
from datetime import date
@shared_task
def send_low_stock_alert():
    low_stock_products = Product.objects.filter(stock_quantity__lte=models.F('reorder_level'))
    if low_stock_products:
        product_list = '\n'.join([f"{p.name}: {p.stock_quantity} left" for p in low_stock_products])
        message = f"The following products have low stock:\n{product_list}"
        send_mail(
            'Low Stock Alert',
            message,
            'dillipkumar21@gmail.com',     # From email
            ['admin@example.com'],         # To email list
            fail_silently=False,
        )
@shared_task
def compute_daily_kpis():
    today = date.today()
    sales_today = Sale.objects.filter(date=today)
    total_revenue = sales_today.aggregate(total=Sum('total_price'))['total'] or 0
    total_orders = sales_today.count()
    avg_order_value = total_revenue / total_orders if total_orders else 0

    top_product = sales_today.values('product__name') \
                             .annotate(quantity_sold=Sum('quantity')) \
                             .order_by('-quantity_sold').first()
    top_selling_product = top_product['product__name'] if top_product else ''

    low_stock_count = Product.objects.filter(stock_quantity__lte=F('reorder_level')).count()

    KPIReport.objects.update_or_create(
        date=today,
        defaults={
            'total_revenue': total_revenue,
            'total_orders': total_orders,
            'avg_order_value': avg_order_value,
            'top_selling_product': top_selling_product,
            'low_stock_count': low_stock_count,
        }
    )