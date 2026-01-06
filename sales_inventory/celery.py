import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales_inventory.settings')

app = Celery('sales_inventory')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()