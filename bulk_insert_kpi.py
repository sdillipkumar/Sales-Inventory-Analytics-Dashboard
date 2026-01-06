from core.models import KPIReport
from datetime import date, timedelta
import random

start_date = date(2025, 10, 1)
bulk_data = []

for i in range(30):  # Create 30 days of reports
    day = start_date + timedelta(days=i)
    total_orders = random.randint(10, 200)
    total_revenue = total_orders * random.uniform(20.0, 100.0)
    avg_order_value = total_revenue / total_orders if total_orders else 0
    top_selling_product = f"Product {random.choice(['A','B','C','D','E'])}"
    low_stock_count = random.randint(0, 10)

    bulk_data.append(KPIReport(
        date=day,
        total_revenue=round(total_revenue, 2),
        total_orders=total_orders,
        avg_order_value=round(avg_order_value, 2),
        top_selling_product=top_selling_product,
        low_stock_count=low_stock_count
    ))

KPIReport.objects.bulk_create(bulk_data)
print("Inserted 30 dummy KPI reports.")
