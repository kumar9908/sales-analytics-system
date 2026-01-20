"""
Main execution file for Sales Analytics System
Covers:
- Part 1: File Handling & Preprocessing
- Part 2: Data Processing & Analytics
- Part 3: API Integration & Data Enrichment
"""

# -------------------- IMPORTS --------------------

from utils.file_handler import read_sales_data, parse_transactions
from utils.data_handler import validate_and_filter
from utils.data_processor import (
    calculate_total_revenue,
    region_wise_sales,
    top_selling_products,
    customer_analysis,
    daily_sales_trend,
    find_peak_sales_day,
    low_performing_products
)
from utils.api_handler import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data,
    save_enriched_data
)

# -------------------- MAIN FUNCTION --------------------

def main():
    print("=" * 60)
    print("SALES ANALYTICS SYSTEM - EXECUTION STARTED")
    print("=" * 60)

    # ==================================================
    # PART 1: FILE HANDLING & PREPROCESSING
    # ==================================================
    print("\n[PART 1] Reading and parsing sales data...")

    raw_lines = read_sales_data("data/sales_data.txt")
    print(f"Raw lines read: {len(raw_lines)}")

    parsed_transactions = parse_transactions(raw_lines)
    print(f"Parsed transactions: {len(parsed_transactions)}")

    # ==================================================
    # PART 1.3: VALIDATION & FILTERING
    # ==================================================
    print("\n[PART 1.3] Validating transactions...")

    valid_transactions, invalid_count, summary = validate_and_filter(
        parsed_transactions
    )

    print("Validation Summary:", summary)

    # ==================================================
    # PART 2: DATA PROCESSING & ANALYTICS
    # ==================================================
    print("\n[PART 2] Running analytics...")

    # ---- Total Revenue ----
    total_revenue = calculate_total_revenue(valid_transactions)
    print(f"\nTotal Revenue: {total_revenue}")

    # ---- Region-wise Sales ----
    region_sales = region_wise_sales(valid_transactions)
    print("\nRegion-wise Sales:")
    for region, data in region_sales.items():
        print(region, "=>", data)

    # ---- Top Selling Products ----
    top_products = top_selling_products(valid_transactions, n=5)
    print("\nTop Selling Products:")
    for product in top_products:
        print(product)

    # ---- Customer Purchase Analysis ----
    customers = customer_analysis(valid_transactions)
    print("\nTop Customer (by spend):")
    first_customer = next(iter(customers.items()))
    print(first_customer)

    # ---- Daily Sales Trend ----
    daily_trend = daily_sales_trend(valid_transactions)
    print("\nDaily Sales Trend (first 3 days):")
    for i, (date, data) in enumerate(daily_trend.items()):
        if i == 3:
            break
        print(date, "=>", data)

    # ---- Peak Sales Day ----
    peak_day = find_peak_sales_day(valid_transactions)
    print("\nPeak Sales Day:")
    print(peak_day)

    # ---- Low Performing Products ----
    low_products = low_performing_products(valid_transactions, threshold=10)
    print("\nLow Performing Products:")
    for product in low_products:
        print(product)

    # ==================================================
    # PART 3: API INTEGRATION & DATA ENRICHMENT
    # ==================================================
    print("\n[PART 3] Fetching product data from API...")

    api_products = fetch_all_products()
    product_mapping = create_product_mapping(api_products)

    print(f"Product mapping created for {len(product_mapping)} products")

    print("\nEnriching sales data with API information...")
    enriched_transactions = enrich_sales_data(
        valid_transactions, product_mapping
    )

    save_enriched_data(enriched_transactions)

    print("\nEnrichment completed successfully.")

    # ==================================================
    # END
    # ==================================================
    print("\n" + "=" * 60)
    print("SALES ANALYTICS SYSTEM - EXECUTION COMPLETED")
    print("=" * 60)


# -------------------- ENTRY POINT --------------------

if __name__ == "__main__":
    main()
