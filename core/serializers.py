from rest_framework import serializers
from core.models import Category, KPIReport,Product,Sale

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class KPIReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPIReport
        fields = '__all__'