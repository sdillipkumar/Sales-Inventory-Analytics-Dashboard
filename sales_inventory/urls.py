"""
URL configuration for sales_inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.urls import path, include
from core.views import KPIReportViewSet, api_root
from rest_framework.routers import DefaultRouter
from core.views import ProductViewSet, CategoryViewSet, SaleViewSet
from core.views import low_stock_alerts
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sales', SaleViewSet)
router.register('kpi-reports', KPIReportViewSet, basename='kpi-report')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root),
    path('api/', include(router.urls)),
    path('api/alerts/low-stock/', low_stock_alerts),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]