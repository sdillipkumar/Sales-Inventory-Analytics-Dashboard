from django.contrib import admin

from core.models import KPIReport, Product, Category, Sale

# Register your models here.
admin.site.register(KPIReport) 
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sale)

