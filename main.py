from utils.file_handler import read_sales_data, parse_transactions
from utils.data_handler import validate_and_filter
from utils.data_processor import *

raw = read_sales_data("data/sales_data.txt")
parsed = parse_transactions(raw)
valid, _, _ = validate_and_filter(parsed)

print("Total Revenue:", calculate_total_revenue(valid))
print("Region Wise:", region_wise_sales(valid))
print("Top Products:", top_selling_products(valid))
print("Customers:", list(customer_analysis(valid).items())[:1])
print("Daily Trend:", list(daily_sales_trend(valid).items())[:1])
print("Peak Day:", find_peak_sales_day(valid))
print("Low Products:"
