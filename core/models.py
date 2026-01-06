from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    reorder_level = models.IntegerField(default=10) #low stock alert level
    warehouse_location = models.CharField(max_length=100, blank=True, null=True) #optional field

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    channel = models.CharField(max_length=50, choices=[("Online","Online"),("Retail","Retail")])#sales channel
    sales_rep = models.CharField(max_length=100, blank=True, null=True)  # Optional

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units on {self.date}"


class KPIReport(models.Model):
    date = models.DateField(unique=True)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    total_orders = models.IntegerField()
    avg_order_value = models.DecimalField(max_digits=15, decimal_places=2)
    top_selling_product = models.CharField(max_length=100)
    low_stock_count = models.IntegerField()

    def __str__(self):
        return (f"KPI Report - {self.date}-->"
                f"  Total Revenue    : ₹{self.total_revenue}-->"
                f"  Total Orders     : {self.total_orders}-->"
                f"  Average Order    : ₹{self.avg_order_value}-->"
                f"  Top Product      : {self.top_selling_product}-->"
                f"  Low Stock Count  : {self.low_stock_count}")
