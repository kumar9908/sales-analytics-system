# main.py

from utils.file_handler import read_sales_data, parse_transactions
from utils.data_handler import validate_and_filter
from utils.api_handler import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data,
    save_enriched_data,
)
from utils.report_generator import generate_sales_report


def main():
    try:
        print("=" * 40)
        print("SALES ANALYTICS SYSTEM")
        print("=" * 40)

        # --------------------------------------------------
        # [1/10] READ SALES DATA
        # --------------------------------------------------
        print("\n[1/10] Reading sales data...")
        raw_lines = read_sales_data("data/sales_data.txt")
        print(f"✓ Successfully read {len(raw_lines)} transactions")

        # --------------------------------------------------
        # [2/10] PARSE & CLEAN DATA
        # --------------------------------------------------
        print("\n[2/10] Parsing and cleaning data...")
        transactions = parse_transactions(raw_lines)
        print(f"✓ Parsed {len(transactions)} records")

        # --------------------------------------------------
        # [3/10] FILTER OPTIONS
        # --------------------------------------------------
        regions = sorted({t["Region"] for t in transactions if t.get("Region")})
        amounts = [
            t["Quantity"] * t["UnitPrice"]
            for t in transactions
            if t.get("Quantity") and t.get("UnitPrice")
        ]

        print("\n[3/10] Filter Options Available:")
        print(f"Regions: {', '.join(regions)}")
        print(f"Amount Range: ₹{min(amounts):,.0f} - ₹{max(amounts):,.0f}")

        apply_filter = input("\nDo you want to filter data? (y/n): ").strip().lower()

        region = None
        min_amount = None
        max_amount = None

        if apply_filter == "y":
            region = input("Enter region (or press Enter to skip): ").strip() or None

            min_amt = input("Enter minimum amount (or press Enter to skip): ").strip()
            max_amt = input("Enter maximum amount (or press Enter to skip): ").strip()

            min_amount = float(min_amt) if min_amt else None
            max_amount = float(max_amt) if max_amt else None

        # --------------------------------------------------
        # [4/10] VALIDATION & FILTERING
        # --------------------------------------------------
        print("\n[4/10] Validating transactions...")
        valid_transactions, invalid_count, summary = validate_and_filter(
            transactions,
            region=region,
            min_amount=min_amount,
            max_amount=max_amount,
        )

        print(
            f"✓ Valid: {len(valid_transactions)} | Invalid: {invalid_count}"
        )

        # --------------------------------------------------
        # [5/10] FETCH PRODUCTS FROM API
        # --------------------------------------------------
        print("\n[5/10] Fetching product data from API...")
        api_products = fetch_all_products()
        product_mapping = create_product_mapping(api_products)
        print(f"✓ Fetched {len(product_mapping)} products")

        # --------------------------------------------------
        # [6/10] ENRICH SALES DATA
        # --------------------------------------------------
        print("\n[6/10] Enriching sales data...")
        enriched_transactions = enrich_sales_data(
            valid_transactions, product_mapping
        )

        enriched_count = sum(
            1 for t in enriched_transactions if t.get("API_Match") is True
        )
        total_count = len(enriched_transactions)

        rate = (enriched_count / total_count * 100) if total_count else 0
        print(f"✓ Enriched {enriched_count}/{total_count} transactions ({rate:.1f}%)")

        # --------------------------------------------------
        # [7/10] SAVE ENRICHED DATA
        # --------------------------------------------------
        print("\n[7/10] Saving enriched data...")
        save_enriched_data(enriched_transactions)
        print("✓ Saved to: data/enriched_sales_data.txt")

        # --------------------------------------------------
        # [8/10] GENERATE REPORT
        # --------------------------------------------------
        print("\n[8/10] Generating report...")
        generate_sales_report(
            valid_transactions,
            enriched_transactions,
            output_file="output/sales_report.txt",
        )
        print("✓ Report saved to: output/sales_report.txt")

        # --------------------------------------------------
        # [9/10] DONE
        # --------------------------------------------------
        print("\n[9/10] Process Complete!")
        print("=" * 40)

    except Exception as e:
        print("\n❌ ERROR OCCURRED")
        print(str(e))


if __name__ == "__main__":
    main()
