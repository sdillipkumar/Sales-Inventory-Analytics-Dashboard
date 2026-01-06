from .models import Product
from django.db import models
def get_low_stock_products():
    return Product.objects.filter(stock_quantity__lte=models.F('reorder_level'))
