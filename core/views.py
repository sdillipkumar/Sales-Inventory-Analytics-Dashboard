from django.shortcuts import render
from rest_framework import viewsets
from .models import KPIReport, Product, Category, Sale
from .serializers import KPIReportSerializer, ProductSerializer, CategorySerializer, SaleSerializer
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .utils import get_low_stock_products
# Create your views here.


def api_root(request):
    return JsonResponse({"message": "Welcome to Sales Inventory API!", 
                         "available_endpoints": ["/api/products/", 
                                                 "/api/categories/", 
                                                 "/api/sales/"]})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
    def perform_create(self, serializer):
        sale = serializer.save()
        product = sale.product
        if sale.quantity > product.stock_quantity:
            raise serializers.ValidationError("Insufficient stock for product!")
        product.stock_quantity -= sale.quantity
        product.save()
@api_view(['GET'])
def low_stock_alerts(request):
    products = get_low_stock_products()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

class KPIReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = KPIReport.objects.all().order_by('-date')
    serializer_class = KPIReportSerializer